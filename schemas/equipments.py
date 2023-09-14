from main import ma
from marshmallow import fields, validate

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
        )

    # tasks = fields.List(fields.Nested("ExpenseSchema", exclude=("user",)))


equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)


