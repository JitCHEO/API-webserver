from main import ma
from marshmallow import fields, validate

class LocationSchema(ma.Schema):
    site = fields.Str(required=True)
    visit_date = fields.Date()
    site_airport = fields.Str()
    state = fields.Str()


    class Meta:
        fields = (
            "id", 
            "site", 
            "visit_date", 
            "site_airport", 
            "state",
        )


    # tasks = fields.List(fields.Nested("ExpenseSchema", exclude=("user",)))


location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)


