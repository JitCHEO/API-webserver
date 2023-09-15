from main import db

class Jira(db.Model):
    __tablename__ = "jiras"

    id = db.Column(db.Integer, primary_key=True)
    issue_title = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=True, default=None)
    service_completion = db.Column(db.Date)
    description = db.Column(db.Text)
    jira_progress = db.Column(db.Text, nullable=True)

    # #FK
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    

    # # Relationships between tables
    equipments = db.relationship(
        "Equipment",
        back_populates="jiras",
        # cascade="all, delete"
    )

    users = db.relationship(
        "User",
        back_populates="jiras",
        # cascade="all, delete"
    )

