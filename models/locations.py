from main import db

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.Text)
    visit_date = db.Column(db.DateTime)
    site_airport = db.Column(db.Text)
    state = db.Column(db.Text)
    
    # equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.id"), nullable=False)

    # users = db.relationship(
    #     "Users",
    #     back_populates="locations"
    # )

    # equipments = db.relationship(
    #     "Equipments",
    #     back_populates="locations",
    # )
