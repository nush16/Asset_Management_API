from main import db

class AssetType(db.Model):
    # define the table name for the db as assets
    __tablename__= "asset_type"
    # Set the primary key
    id = db.Column(db.Integer,primary_key=True)
    # the rest of the attributes/columns
    description  = db.Column(db.String()) 
    # link to manufacturers 
    manufacturer = db.relationship("Manufacturer", backref = "asset_type", cascade="all, delete")
    # link to assets
    asset_id = db.Column(db.Integer, db.ForeignKey("assets.id"), nullable =False)
    