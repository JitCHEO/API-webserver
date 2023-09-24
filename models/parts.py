from main import db

class Part(db.Model):
    __tablename__ = "parts"

    id = db.Column(db.Integer, primary_key=True)
    # Name/description of parts
    part_name = db.Column(db.Text)
    # Date the parts was purchased
    purchase_date = db.Column(db.DateTime)
    # Additional information/description of the partts purchased
    description = db.Column(db.Text)
    # Total amount spent on getting the parts
    amount_spent = db.Column(db.Numeric(precision=10, scale=2))  # 10 digits total with 2 decimal places
    
    # FK
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.id"))
    

    # Relationships between tables
    equipments = db.relationship(
        "Equipment",
        back_populates="parts",
    )

