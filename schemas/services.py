from main import ma
from marshmallow import fields, validate

class ServiceSchema(ma.Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=400))
    type_service = fields.Str(required=True)
    service_date = fields.Date()
    description = fields.Str()

    class Meta:
        fields =(
            "id",
            "type_service",
            "service_date",
            "description",
            "state", 
            "equipments"
        )    
    equipments = fields.Nested("EquipmentSchema")
    
service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)


