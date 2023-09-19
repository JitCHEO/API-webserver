from main import ma
from marshmallow import fields, validate

class InductionSchema(ma.Schema):
    expiry_date = fields.Date()
    documents_required = fields.Str()
    description = fields.Str()
    

    class Meta:
        fields = (
            "id",
            "expiry_date",
            "documents_required",
            "description",
            "locations"
        )

    locations = fields.Nested("LocationSchema")



induction_schema = InductionSchema()
inductions_schema = InductionSchema(many=True)


