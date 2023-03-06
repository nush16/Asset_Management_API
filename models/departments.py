from main import db

class Department(db.Model):
    # define the table name for the db as departments
    __tablename__= "Departments"
    # Set the primary key
    id = db.Column(db.Integer,primary_key=True)
    # the rest of the attributes/columns
    building_number = db.Column(db.String())
    room_number = db.Column(db.String())
    address = db.Column(db.String())
    # Foreign key to link to employees (refer to primary key of the employee)
    employees = db.relationship("Employee", backref = "departments")