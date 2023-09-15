from main import db

class Equipment(db.Model):
    __tablename__ = "equipments"

    id = db.Column(db.Integer, primary_key=True)
    equipment_number = db.Column(db.Text)
    type_equipment = db.Column(db.Text)
    description = db.Column(db.Text)
    
    # # FK 
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # locations_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
  

    # # Relationships between tables
    user = db.relationship(
        "User",
        back_populates="equipments"
    )

    # services = db.relationship(
    #     "Service",
    #     back_populates="equipments",
    #     # cascade="all, delete"
    # )

    parts = db.relationship(
        "Part",
        back_populates="equipments",
        # cascade="all, delete"
    )

    locations = db.relationship(
        "Location",
        back_populates="equipments",
        cascade="all, delete"
    )

    jiras = db.relationship(
        "Jira",
        back_populates="equipments",
        # cascade="all, delete"
    )


