from flask import Blueprint, jsonify, request
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from main import db
from models.users import User
from models.jiras import Jira
from schemas.jiras import jira_schema, jiras_schema

# /jira
jiras = Blueprint("jira", __name__, url_prefix="/jiras")

@jiras.errorhandler(ValidationError)
def key_error_handler(e):
    return jsonify({"error": f"Validation Error - `{e}`"}), 400

# /jiras -> list of jiras
@jiras.route("/", methods=["GET"])
def get_jiras():
    q = db.select(Jira)
    jiras = db.session.scalars(q)
    return jsonify(jiras_schema.dump(jiras))
    
# /jiras/<id> -> show jira with id
@jiras.route("/<int:jira_id>", methods=["GET"])
def get_jira(jira_id: int):
    q = db.select(Jira).filter_by(id=jira_id)
    jira = db.session.scalar(q)
    response = jira_schema.dump(jira)

    if response:
        return jsonify(response)

    return jsonify(message=f"Jira with id=`{jira_id}` not found")

    
# /jiras/<id> -> delete jira with id
@jiras.route("/<int:jira_id>", methods=["DELETE"])
@jwt_required()
def delete_jira(jira_id: int):
    email = get_jwt_identity()
    statement = db.select(User).filter_by(email=email)
    user = db.session.scalar(statement)

    q = db.select(Jira).filter_by(user_id=user.id)
    jira = db.session.scalar(q)
    response = jira_schema.dump(jira)

    # the old without jwt_required
    # q = db.select(Jira).filter_by(id=jira_id)
    # jira = db.session.scalar(q)
    # response = jira_schema.dump(jira)

    if response:
        db.session.delete(jira)
        db.session.commit()
        return jsonify(message=f"Jira with id=`{jira_id}` deleted successfully!")

    return jsonify(message=f"Cannot delete jira with id=`{jira_id}`. Not found")

# /jiras -> Creating a jira
@jiras.route("/", methods=["POST"])
@jwt_required()
def create_jiras():
    email = get_jwt_identity()
    statement = db.select(User).filter_by(email=email)
    user = db.session.scalar(statement)

    jira_json = jira_schema.load(request.json)
    jira = Jira(**jira_json)
    jira.user_id = user.id
    db.session.add(jira)
    db.session.commit()

    return jsonify(jira_schema.dump(jira))

# /jiras/<id> -> Updating a jira with id
@jiras.route("/<int:jira_id>", methods=["PUT"])
def update_jiras(jira_id: int):
    q = db.select(Jira).filter_by(id=jira_id)
    jira = db.session.scalar(q)
    response = jira_schema.dump(jira)

    if response:
        jira_json = jira_schema.load(request.json)
        jira.issue_title = jira_json["issue_title"]
        jira.created_at = jira_json["created_at"]
        jira.service_completion = jira_json["service_completion"]
        jira.description = jira_json["description"]
        jira.jira_progress = jira_json["jira_progress"]
        jira.user_id = jira_json["user_id"]
        db.session.commit()
        return jsonify(jira_schema.dump(jira))

    return jsonify(message=f"Cannot update jira with id=`{jira_id}`. Not found")
