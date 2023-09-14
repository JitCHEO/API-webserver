from main import db

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.Text)
    visit_date = db.Column(db.DateTime)
    site_airport = db.Column(db.Text)
    state = db.Column(db.Text)
    
    #FK
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.id"), nullable=False)

    # Tables relationships
    users = db.relationship(
        "User",
        back_populates="locations"
    )

    # equipments = db.relationship(
    #     "Equipments",
    #     back_populates="locations",
    # )
