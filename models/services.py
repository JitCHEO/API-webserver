from main import db

class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    type_service = db.Column(db.Text)
    service_date = db.Column(db.DateTime)
    description = db.Column(db.Text)
    state = db.Column(db.Text)

#    #FK
#     equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.id"), nullable=False)
#     part_id = db.Column(db.Integer, db.ForeignKey("parts.id"), nullable=False)

#     # Relationships between tables
#     equipments = db.relationship(
#         "Equipments",
#         back_populates="services",
#         # cascade="all, delete"
#     )




