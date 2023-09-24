from main import db

class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    # type/category if service
    type_service = db.Column(db.Text)
    # datatime service was performed
    service_date = db.Column(db.DateTime)
    # Description or details of the servicing done
    description = db.Column(db.Text)
    # Which state that the service was done
    state = db.Column(db.Text)

    # FK
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.id"))

    # Relationships between tables
    equipments = db.relationship(
        "Equipment",
        back_populates="services"
    )




