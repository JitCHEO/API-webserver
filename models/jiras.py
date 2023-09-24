from main import db

class Jira(db.Model):
    __tablename__ = "jiras"

    id = db.Column(db.Integer, primary_key=True)
    # Title or summary of the JIRA issue
    issue_title = db.Column(db.Text)
    # Date & time JIRA issue was created
    created_at = db.Column(db.DateTime, nullable=True, default=None)
    # Date when service related to the JIRA was completed
    service_completion = db.Column(db.Date)
    # Detailed description of JIRA issue
    description = db.Column(db.Text)
    # The progress status of the JIRA issue
    jira_progress = db.Column(db.Text, nullable=True)

    # FK
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    

    # Relationships between tables
    equipments = db.relationship(
        "Equipment",
        back_populates="jiras"
    )

    users = db.relationship(
        "User",
        back_populates="jiras"
    )

