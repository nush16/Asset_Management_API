from main import db

class Asset(db.Model):
    # define the table name for the db as assets
    __tablename__= "assets"
    # Set the primary key
    asset_id = db.Column(db.Integer,primary_key=True)
    # the rest of the attributes/columns
    serial_number  = db.Column(db.String(), nullable=False) 
    date_purchased = db.Column(db.Date(), nullable=False) 
     # link to asset_type
    asset_type_id = db.relationship("AssetType", backref = "asset", cascade= "all, delete")
    # link to employees 
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.employee_id"), nullable =False)
   
