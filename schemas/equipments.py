from main import ma
from marshmallow import fields

class EquipmentSchema(ma.Schema):
    equipment_number = fields.Str(required=True)
    type_equipment = fields.Str()
    description = fields.Str()

    class Meta:
        fields = (
            "id",
            "equipment_number",
            "type_equipment",
            "description",
            "user_id",
            "user"
        )
    user = fields.Nested("UserSchema")




equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)


