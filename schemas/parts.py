from main import ma
from marshmallow import fields, validate

class PartSchema(ma.Schema):
    part_name = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    purchase_date = fields.Date()
    description = fields.Str()
    amount_spent = fields.Float()
    # state = fields.String(load_default='Not Started', validate=validate.OneOf(["Not Started", "In Progress", "Completed"]))

    class Meta:
        fields = (
            "id", 
            "part_name", 
            "purchase_date", 
            "description", 
            "amount_spent"
        )

    # tasks = fields.List(fields.Nested("ExpenseSchema", exclude=("user",)))



part_schema = PartSchema()
parts_schema = PartSchema(many=True)


