from main import db

class Equipment(db.Model):
    __tablename__ = "equipments"

    id = db.Column(db.Integer, primary_key=True)
    equipment_number = db.Column(db.Text)
    type_equipment = db.Column(db.Text)
    description = db.Column(db.Text)
    
    # # FK 
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
     

    # # Relationships between tables
    user = db.relationship(
        "User",
        back_populates="equipments"
    )

    services = db.relationship(
        "Service",
        back_populates="equipments"
    )

    parts = db.relationship(
        "Part",
        back_populates="equipments"
    )

    locations = db.relationship(
        "Location",
        back_populates="equipments"
    )

    jiras = db.relationship(
        "Jira",
        back_populates="equipments"
    )


