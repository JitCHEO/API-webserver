from flask import Blueprint, jsonify, request
from marshmallow.exceptions import ValidationError

from main import db
from models.parts import Part
from schemas.parts import part_schema, parts_schema

# /part
parts = Blueprint("part", __name__, url_prefix="/parts")

@parts.errorhandler(ValidationError)
def key_error_handler(e):
    return jsonify({"error": f"Validation Error - `{e}`"}), 400

# /parts -> list of parts
@parts.route("/", methods=["GET"])
def get_parts():
    q = db.select(Part)
    parts = db.session.scalars(q)
    return jsonify(parts_schema.dump(parts))
    
# /parts/<id> -> show part with id
@parts.route("/<int:part_id>", methods=["GET"])
def get_part(part_id: int):
    q = db.select(Part).filter_by(id=part_id)
    part = db.session.scalar(q)
    response = part_schema.dump(part)

    if response:
        return jsonify(response)

    return jsonify(message=f"Part with id=`{part_id}` not found")

    
# /parts/<id> -> delete part with id
@parts.route("/<int:part_id>", methods=["DELETE"])
def delete_part(part_id: int):
    q = db.select(Part).filter_by(id=part_id)
    part = db.session.scalar(q)
    response = part_schema.dump(part)

    if response:
        db.session.delete(part)
        db.session.commit()
        return jsonify(message=f"Part with id=`{part_id}` deleted successfully!")

    return jsonify(message=f"Cannot delete part with id=`{part_id}`. Not found")

# /parts -> Creating a part
@parts.route("/", methods=["POST"])
def create_parts():
    part_json = part_schema.load(request.json)
    part = Part(**part_json)
    db.session.add(part)
    db.session.commit()

    return jsonify(part_schema.dump(part))

# /parts/<id> -> Updating a part with id
@parts.route("/<int:part_id>", methods=["PUT"])
def update_parts(part_id: int):
    q = db.select(Part).filter_by(id=part_id)
    part = db.session.scalar(q)
    response = part_schema.dump(part)

    if response:
        part_json = part_schema.load(request.json)
        part.part_name = part_json["part_name"]
        part.purchase_date = part_json["purchase_date"]
        part.description = part_json["description"]
        part.amount_spent = part_json["amount_spent"]
    
        db.session.commit()
        return jsonify(part_schema.dump(part))

    return jsonify(message=f"Cannot update part with id=`{part_id}`. Not found")

