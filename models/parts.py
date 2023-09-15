from main import db

class Part(db.Model):
    __tablename__ = "parts"

    id = db.Column(db.Integer, primary_key=True)

    part_name = db.Column(db.Text)
    purchase_date = db.Column(db.DateTime)
    description = db.Column(db.Text)
    amount_spent = db.Column(db.Integer)
    
    # #FK
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.id"))
    

    # # Relationships between tables
    equipments = db.relationship(
        "Equipment",
        back_populates="parts",
        # cascade="all, delete"
    )

