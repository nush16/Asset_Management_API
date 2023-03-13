from main import db

class Department(db.Model):
    # define the table name for the db as departments
    __tablename__= "departments"
    # Set the primary key
    department_id = db.Column(db.Integer, primary_key = True)
    # the rest of the attributes/columns
    department_name = db.Column(db.String(), nullable = False)
    building_number = db.Column(db.Integer(), nullable = False)
    address = db.Column(db.String(), nullable = False)
    # Foreign key to link to employees (refer to primary key of the employee)
    employees = db.relationship("Employee", backref = "departments", cascade= "all, delete")