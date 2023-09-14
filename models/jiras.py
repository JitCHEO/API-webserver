from main import db

class Jira(db.Model):
    __tablename__ = "jiras"

    id = db.Column(db.Integer, primary_key=True)
    issue_title = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=True, default=None)
    service_completion = db.Column(db.Date)
    description = db.Column(db.Text)
    jira_progress = db.Column(db.Text, nullable=True)

    #FK
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Relationships between tables
    equipments = db.relationship(
        "Equipments",
        back_populates="jiras",
        # cascade="all, delete"
    )

    users = db.relationship(
        "Users",
        back_populates="jiras",
        # cascade="all, delete"
    )

    services = db.relationship(
        "Services",
        back_populates="jiras",
        # cascade="all, delete"
    )

    jiras = db.relationship(
        "Jiras",
        back_populates="jiras",
        # cascade="all, delete"
    )
