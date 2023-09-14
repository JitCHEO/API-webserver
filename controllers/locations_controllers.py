from flask import Blueprint, jsonify, request
from marshmallow.exceptions import ValidationError

from main import db
from models.locations import Location
from schemas.locations import location_schema, locations_schema

# /user
locations = Blueprint("location", __name__, url_prefix="/locations")

@locations.errorhandler(ValidationError)
def key_error_handler(e):
    return jsonify({"error": f"Validation Error - `{e}`"}), 400

# /locations -> list of locations
@locations.route("/", methods=["GET"])
def get_locations():
    q = db.select(Location)
    locations = db.session.scalars(q)
    return jsonify(locations_schema.dump(locations))
    
# /locations/<id> -> show location with id
@locations.route("/<int:location_id>", methods=["GET"])
def get_location(location_id: int):
    q = db.select(Location).filter_by(id=location_id)
    location = db.session.scalar(q)
    response = location_schema.dump(location)

    if response:
        return jsonify(response)

    return jsonify(message=f"Location with id=`{location_id}` not found")

    
# /locations/<id> -> delete location with id
@locations.route("/<int:location_id>", methods=["DELETE"])
def delete_location(location_id: int):
    q = db.select(Location).filter_by(id=location_id)
    location = db.session.scalar(q)
    response = location_schema.dump(location)

    if response:
        db.session.delete(location)
        db.session.commit()
        return jsonify(message=f"Location with id=`{location_id}` deleted successfully!")

    return jsonify(message=f"Cannot delete location with id=`{location_id}`. Not found")

# /locations -> Creating a location
@locations.route("/", methods=["POST"])
def create_locations():
    location_json = location_schema.load(request.json)
    location = Location(**location_json)
    db.session.add(location)
    db.session.commit()

    return jsonify(location_schema.dump(location))

# /locations/<id> -> Updating a location with id
@locations.route("/<int:location_id>", methods=["PUT"])
def update_locations(location_id: int):
    q = db.select(Location).filter_by(id=location_id)
    location = db.session.scalar(q)
    response = location_schema.dump(location)

    if response:
        location_json = location_schema.load(request.json)
        location.site = location_json["site"]
        location.visit_date = location_json["visit_date"]
        location.site_airport = location_json["site_airport"]
        location.state = location_json["state"]
        location.user_id = location_json["user_id"]
        db.session.commit()
        return jsonify(location_schema.dump(location))

    return jsonify(message=f"Cannot update location with id=`{location_id}`. Not found")
      