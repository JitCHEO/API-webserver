from main import ma
from marshmallow import fields, validate

class JiraSchema(ma.Schema):
    issue_title = fields.Str(required=True)
    created_at = fields.Date()
    service_completion = fields.Date()
    description = fields.Str()
    jira_progress = fields.String(load_default='Not Started', validate=validate.OneOf(["Not Started", "In Progress", "Completed"]))

    class Meta:
        fields = (
            "id",
            "issue_title",
            "created_at",
            "service_completion",
            "description",
            "jira_progress",
            "equipments",
            "user_id"
        )

    equipments = fields.Nested("EquipmentSchema", excludes=["user_id"])



jira_schema = JiraSchema()
jiras_schema = JiraSchema(many=True)


