from main import ma
from marshmallow import fields, validate

class PartSchema(ma.Schema):
    part_name = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    purchase_date = fields.Date()
    description = fields.Str()
    amount_spent = fields.Float()

    class Meta:
        fields = (
            "id", 
            "part_name", 
            "purchase_date", 
            "description", 
            "amount_spent",
            "equipments"
        )
    equipments = fields.Nested("EquipmentSchema")
    

part_schema = PartSchema()
parts_schema = PartSchema(many=True)


