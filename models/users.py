from main import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    services = db.relationship(
        "services",
        back_populates="users",
        # cascade="all, delete"
    )

    parts = db.relationship(
        "parts",
        back_populates="users",
        # cascade="all, delete"
    )


    locations = db.relationship(
        "Locations",
        back_populates="user",
        # cascade="all, delete"
    )

    jiras = db.relationship(
        "Jiras",
        back_populates="user",
        # cascade="all, delete"
    )


    equipments = db.relationship(
        "Equipments",
        back_populates="user",
        # cascade="all, delete"
    )
