from main import db

class Asset(db.Model):
    # define the table name for the db as assets
    __tablename__= "Assets"
    # Set the primary key
    id = db.Column(db.Integer,primary_key=True)
    # the rest of the attributes/columns
    description  = db.Column(db.String()) 
    # link to employees 
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable =False)
    asset_manufacturer_id = db.Column(db.String())