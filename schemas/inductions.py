from main import ma
from marshmallow import fields

class InductionSchema(ma.Schema):
    expiry_date = fields.Date()
    documents_required = fields.Str()
    description = fields.Str()
    

    class Meta:
        fields = (
            "expiry_date",
            "documents_required",
            "description",
            "locations"
        )

    locations = fields.Nested("LocationSchema", exclude=["equipments"])



induction_schema = InductionSchema()
inductions_schema = InductionSchema(many=True)


