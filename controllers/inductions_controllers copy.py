from flask import Blueprint, jsonify, request
from marshmallow.exceptions import ValidationError

from main import db
from models.inductions import Induction
from schemas.inductions import induction_schema, inductions_schema

# /induction
inductions = Blueprint("induction", __name__, url_prefix="/inductions")

@inductions.errorhandler(ValidationError)
def key_error_handler(e):
    return jsonify({"error": f"Validation Error - `{e}`"}), 400

# /inductions -> list of inductions
@inductions.route("/", methods=["GET"])
def get_inductions():
    q = db.select(Induction)
    inductions = db.session.scalars(q)
    return jsonify(inductions_schema.dump(inductions))
    
# /inductions/<id> -> show induction with id
@inductions.route("/<int:induction_id>", methods=["GET"])
def get_induction(induction_id: int):
    q = db.select(Induction).filter_by(id=induction_id)
    induction = db.session.scalar(q)
    response = induction_schema.dump(induction)

    if response:
        return jsonify(response)

    return jsonify(message=f"Induction with id=`{equipment_id}` not found")

    
# /inductions/<id> -> delete induction with id
@inductions.route("/<int:induction_id>", methods=["DELETE"])
def delete_induction(induction_id: int):
    q = db.select(Induction).filter_by(id=induction_id)
    induction = db.session.scalar(q)
    response = induction_schema.dump(induction)

    if response:
        db.session.delete(induction)
        db.session.commit()
        return jsonify(message=f"Induction with id=`{induction_id}` deleted successfully!")

    return jsonify(message=f"Cannot delete induction with id=`{induction_id}`. Not found")

# /inductions -> Creating a induction
@inductions.route("/", methods=["POST"])
def create_inductions():
    induction_json = induction_schema.load(request.json)
    induction = Induction(**induction_json)
    db.session.add(induction)
    db.session.commit()

    return jsonify(induction_schema.dump(induction))

# /inductions/<id> -> Updating a induction with id
@inductions.route("/<int:induction_id>", methods=["PUT"])
def update_inductions(induction_id: int):
    q = db.select(Induction).filter_by(id=induction_id)
    induction = db.session.scalar(q)
    response = induction_schema.dump(induction)

    if response:
        induction_json = induction_schema.load(request.json)
        induction.expiry_date = induction_json["expiry_date"]
        induction.documents_required = induction_json["documents_required"]
        induction.description = induction_json["description"]
        induction.location = induction_json["location"]
        db.session.commit()
        return jsonify(induction_schema.dump(induction))

    return jsonify(message=f"Cannot update induction with id=`{induction_id}`. Not found")
