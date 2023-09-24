from main import ma
from marshmallow import fields, validate

class UserSchema(ma.Schema):
    """
    Schema for serialize & deserialize the user data.

    Meta: 
    - A tuple of field name to include in the serialized output. 
    """
    email = fields.Email(
        required=True,
        validate=validate.Length(min=6, max=25, error="Careful this email is valid")
    )

    class Meta:
        fields = (
            "id",
            "email",
            "password",
            "admin",
        ) 



user_schema = UserSchema()
users_schema = UserSchema(many=True)


