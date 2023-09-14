from main import ma
from marshmallow import fields, validate

class ServiceSchema(ma.Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    type_service = fields.Str(required=True)
    service_date = fields.Date()
    description = fields.Str()
    # state = fields.String(load_default='Not Started', validate=validate.OneOf(["Not Started", "In Progress", "Completed"]))

    class Meta:
        fields =(
            "id",
            "type_service",
            "service_date",
            "description",
            "state", 
        )    

    # tasks = fields.List(fields.Nested("ExpenseSchema", exclude=("user",)))


service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)


