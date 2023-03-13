from main import db

class Employee(db.Model):
    # define the table name for the db as employees
    __tablename__= "employees"
    # Set the primary key
    id = db.Column(db.Integer,primary_key=True)
    # rest of the attributes/columns
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email_address = db.Column(db.String(), nullable=False, unique=True)
    contact_number = db.Column(db.Integer(), nullable=False, unique=True)
    room_number = db.Column(db.Integer(), nullable = False)
    position = db.Column(db.String(), nullable=False)
    # There can be many employees in a department - foreign key to link to departments
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable =False)
    # an employee can have many assets - foreign key to link to assets
    assets = db.relationship("Asset", backref = "employees", cascade="all, delete")