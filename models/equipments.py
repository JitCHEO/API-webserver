from main import db

class Equipment(db.Model):
    __tablename__ = "equipments"

    id = db.Column(db.Integer, primary_key=True)
    equipment_number = db.Column(db.Text)
    type_equipment = db.Column(db.Text)
    description = db.Column(db.Text)
    
    # FK 
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    locations_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)

    # Relationships between tables
    users = db.relationship(
        "Users",
        back_populates="equipments",
        # cascade="all, delete"
    )

    services = db.relationship(
        "services",
        back_populates="equipments",
        # cascade="all, delete"
    )

    parts = db.relationship(
        "parts",
        back_populates="equipments",
        # cascade="all, delete"
    )


    locations = db.relationship(
        "Locations",
        back_populates="equipments",
        # cascade="all, delete"
    )

    jiras = db.relationship(
        "Jiras",
        back_populates="equipments",
        # cascade="all, delete"
    )


