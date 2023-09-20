from main import db

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.Text)
    visit_date = db.Column(db.DateTime)
    site_airport = db.Column(db.Text)
    state = db.Column(db.Text)
    
    #FK
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