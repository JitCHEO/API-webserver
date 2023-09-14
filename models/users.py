from main import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    equipments = db.relationship(
        "Equipment",
        back_populates="users",
        # cascade="all, delete"
    )

    jiras = db.relationship(
        "Jira",
        back_populates="users",
        # cascade="all, delete"
    )

