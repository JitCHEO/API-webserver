from flask import Blueprint, jsonify, request
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError 

from main import db
from models.services import Service
from schemas.services import service_schema, services_schema

# /service
services = Blueprint("service", __name__, url_prefix="/services")

@services.errorhandler(ValidationError)
def key_error_handler(e):
    return jsonify({"error": f"Validation Error - `{e}`"}), 400

# /Service -> list of Service
@services.route("/", methods=["GET"])
def get_services():
    q = db.select(Service)
    services = db.session.scalars(q)
    return jsonify(services_schema.dump(services))
    
# /services/<id> -> show service with id
@services.route("/<int:service_id>", methods=["GET"])
def get_service(service_id: int):
    q = db.select(Service).filter_by(id=service_id)
    service = db.session.scalar(q)
    response = service_schema.dump(service)

    if response:
        return jsonify(response)

    return jsonify(message=f"Service with id=`{service_id}` not found")

    
# /services/<id> -> delete service with id
@services.route("/<int:service_id>", methods=["DELETE"])
def delete_service(service_id: int):
    q = db.select(Service).filter_by(id=service_id)
    service = db.session.scalar(q)
    response = service_schema.dump(service)

    if response:
        db.session.delete(service)
        db.session.commit()
        return jsonify(message=f"Service with id=`{service_id}` deleted successfully!")

    return jsonify(message=f"Cannot delete service with id=`{service_id}`. Not found")

# /services -> Creating a service
@services.route("/", methods=["POST"])
def create_services():
    try:
        service_json = service_schema.load(request.json)
        service = Service(**service_json)
        db.session.add(service)
        db.session.commit()

        return jsonify(service_schema.dump(service)), 201
    
    except IntegrityError as e:
        db.session.rollback()  # Rollback the transaction
        return jsonify({"error": "User creation failed due to a existing service"}), 400

# /services/<id> -> Updating a service with id
@services.route("/<int:service_id>", methods=["PUT"])
def update_services(service_id: int):
    q = db.select(Service).filter_by(id=service_id)
    service = db.session.scalar(q)
    response = service_schema.dump(service)

    if response:
        service_json = service_schema.load(request.json)
        service.type_service = service_json["type_service"]
        service.service_date = service_json["service_date"]
        service.description = service_json["description"]
        service.state = service_json["state"]        
        db.session.commit()
        return jsonify(service_schema.dump(service))

    return jsonify(message=f"Cannot update service with id=`{service_id}`. Not found")

    