from main import db

class AssetType(db.Model):
    # define the table name for the db as assets
    __tablename__= "Asset_Types"
    # Set the primary key
    id = db.Column(db.Integer,primary_key=True)
    # the rest of the attributes/columns
    description  = db.Column(db.String()) 
    # link to employees 
    # manufacturer_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable =False)
    # link to manufacturers
    asset_id = db.Column(db.Integer, db.ForeignKey("Assets.id"), nullable =False)
    