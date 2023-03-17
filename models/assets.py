from main import db

class Asset(db.Model):
    # define the table name for the db as assets
    __tablename__= "assets"
    # Set the primary key
    asset_id = db.Column(db.Integer,primary_key=True)
    # the rest of the attributes/columns
    asset_name = db.Column(db.String(), nullable=False) 
    serial_number  = db.Column(db.String(), nullable=False) 
    date_purchased = db.Column(db.Date(), nullable=False)
    asset_type = db.Column(db.String()) 
    service_job_id = db.relationship("ServiceJob", backref = "asset", cascade= "all, delete") 
     # link to asset_type
    manufacturer_id = db.relationship("Manufacturer", backref = "asset", cascade= "all, delete")
    # link to employees 
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.employee_id"), nullable =False)
   
