from main import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    # email address for user being unique
    email = db.Column(db.Text, nullable=False, unique=True)
    # password of user to be hashed
    password = db.Column(db.Text, nullable=False)
    #Indicating if user is an admin,default is false
    admin = db.Column(db.Boolean, nullable=False, default=False)
    is_admin = db.Column(db.Boolean, default=False)


    # Tables relationships
    # Relationships with Equipment table
    equipments = db.relationship(
        "Equipment",
        back_populates="user"
    )

    # Relationships with JIRA table
    jiras = db.relationship(
        "Jira",
        back_populates="users"
    )

