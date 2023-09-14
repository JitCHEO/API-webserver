from flask import Blueprint, jsonify, request
from marshmallow.exceptions import ValidationError

from main import db
from models.equipments import Equipment
from schemas.equipments import equipment_schema, equipments_schema

# /equipment
equipments = Blueprint("equipment", __name__, url_prefix="/equipments")

@equipments.errorhandler(ValidationError)
def key_error_handler(e):
    return jsonify({"error": f"Validation Error - `{e}`"}), 400

# /equipments -> list of equipments
@equipments.route("/", methods=["GET"])
def get_equipments():
    q = db.select(Equipment)
    equipments = db.session.scalars(q)
    return jsonify(equipments_schema.dump(equipments))
    
# /equipments/<id> -> show equipment with id
@equipments.route("/<int:equipment_id>", methods=["GET"])
def get_equipment(equipment_id: int):
    q = db.select(Equipment).filter_by(id=equipment_id)
    equipment = db.session.scalar(q)
    response = equipment_schema.dump(equipment)

    if response:
        return jsonify(response)

    return jsonify(message=f"Equipment with id=`{equipment_id}` not found")

    
# /equipments/<id> -> delete equipment with id
@equipments.route("/<int:equipment_id>", methods=["DELETE"])
def delete_equipment(equipment_id: int):
    q = db.select(Equipment).filter_by(id=equipment_id)
    equipment = db.session.scalar(q)
    response = equipment_schema.dump(equipment)

    if response:
        db.session.delete(equipment)
        db.session.commit()
        return jsonify(message=f"Equipment with id=`{equipment_id}` deleted successfully!")

    return jsonify(message=f"Cannot delete equipment with id=`{equipment_id}`. Not found")

# /equipments -> Creating a equipment
@equipments.route("/", methods=["POST"])
def create_equipments():
    equipment_json = equipment_schema.load(request.json)
    equipment = Equipment(**equipment_json)
    db.session.add(equipment)
    db.session.commit()

    return jsonify(equipment_schema.dump(equipment))

# /equipments/<id> -> Updating a equipment with id
@equipments.route("/<int:equipment_id>", methods=["PUT"])
def update_equipments(equipment_id: int):
    q = db.select(Equipment).filter_by(id=equipment_id)
    equipment = db.session.scalar(q)
    response = equipment_schema.dump(equipment)

    if response:
        equipment_json = equipment_schema.load(request.json)
        equipment.equipment_number = equipment_json["equipment_number"]
        equipment.type_equipment = equipment_json["type_equipment"]
        equipment.description = equipment_json["description"]
        db.session.commit()
        return jsonify(equipment_schema.dump(equipment))

    return jsonify(message=f"Cannot update equipment with id=`{equipment_id}`. Not found")
