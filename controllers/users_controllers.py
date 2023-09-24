from flask import Blueprint, jsonify, request
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError 

from main import db
from models.users import User
from schemas.users import user_schema, users_schema

# /user
# Create a Flask Blueprint for user-related routes
users = Blueprint("user", __name__, url_prefix="/users")

# Error handler for validation errors
@users.errorhandler(ValidationError)
def key_error_handler(e):
    """
    Handle validation errors and return a JSON response with a 400 status code.
    return: JSON response with an error message.
    """
    return jsonify({"error": f"Validation Error - `{e}`"}), 400

# /users -> list of users
@users.route("/", methods=["GET"])
def get_users():
    """
    Get a list of all users.

    Returns:
    Flask Response: JSON response containing the list of users.
    """
    q = db.select(User)
    users = db.session.scalars(q)
    return jsonify(users_schema.dump(users))
    
# /users/<id> -> show user with id
@users.route("/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)
    response = user_schema.dump(user)

    if response:
        return jsonify(response)

    return jsonify(message=f"User with id=`{user_id}` not found")

    
# /users/<id> -> delete user with id
@users.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)
    response = user_schema.dump(user)

    if response:
        db.session.delete(user)
        db.session.commit()
        return jsonify(message=f"User with id=`{user_id}` deleted successfully!")

    return jsonify(message=f"Cannot delete user with id=`{user_id}`. Not found")

# /users -> Creating a user
@users.route("/", methods=["POST"])
def create_users():
    try:
        user_json = user_schema.load(request.json)
        user = User(**user_json)
        db.session.add(user)
        db.session.commit()

        return jsonify(user_schema.dump(user)), 201

    except IntegrityError as e:
        db.session.rollback()  # Rollback the transaction
        return jsonify({"error": "User creation failed due to a existing user"}), 400


# /users/<id> -> Updating a user with id
@users.route("/<int:user_id>", methods=["PUT"])
def update_users(user_id: int):
    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)
    response = user_schema.dump(user)

    if response:
        user_json = user_schema.load(request.json)
        user.email = user_json["email"]
        user.password = user_json["password"]
        user.admin = user_json["admin"]
        db.session.commit()
        return jsonify(user_schema.dump(user))

    return jsonify(message=f"Cannot update user with id=`{user_id}`. Not found")
