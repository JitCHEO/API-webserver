from main import db

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    # Name of the site location
    site = db.Column(db.Text)
    # Date of the visit to the location
    visit_date = db.Column(db.DateTime)
    # Airport that is associated
    site_airport = db.Column(db.Text)
    # State or region where location is located
    state = db.Column(db.Text)
    
    # FK
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.id"))


    # Tables relationships
    equipments = db.relationship(
        "Equipment",
        back_populates="locations",
    )

    inductions = db.relationship(
        "Induction",
        back_populates="locations",
    )