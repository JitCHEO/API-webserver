from main import ma
from marshmallow import fields, validate

class InductionSchema(ma.Schema):
    expiry_date = fields.Date()
    documents_required = fields.Str()
    description = fields.Str()
    induction_progress = fields.String(load_default='Not Started', validate=validate.OneOf(["Not Started", "In Progress", "Completed"]))
    

    class Meta:
        fields = (
            "id",
            "expiry_date",
            "documents_required",
            "description",
            "locations",
            "induction_progress"

        )

    locations = fields.Nested("LocationSchema", exclude=["equipments"])



induction_schema = InductionSchema()
inductions_schema = InductionSchema(many=True)


