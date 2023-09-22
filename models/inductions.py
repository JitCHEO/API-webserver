from main import db

class Induction(db.Model):
    __tablename__ = "inductions"

    id = db.Column(db.Integer, primary_key=True)
    expiry_date = db.Column(db.DateTime, nullable=True, default=None)
    documents_required = db.Column(db.Text)
    description = db.Column(db.Text)
    induction_progress = db.Column(db.Text, nullable=True)
   

    # #FK
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    

    # # Relationships between tables
    locations = db.relationship(
        "Location",
        back_populates="inductions",
    )
    

