from main import db

class User(db.Model):
    # define the table name
    __tablename__ = "users"
    # Set the primary key
    id = db.Column(db.Integer, primary_key=True)
    # the rest of the attributes/columns
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
