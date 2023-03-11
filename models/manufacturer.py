from main import db

class Manufacturer(db.Model):
    # define the table name for the db as asset_manufacturers
    __tablename__= "Manufacturers"
    # Set the primary key
    id = db.Column(db.Integer,primary_key=True)
    # the rest of the attributes/columns
    manufacturer_name = db.Column(db.String())
    manufacturer_contact_number = db.Column(db.Integer())
    manufacturer_email = db.Column(db.String())
    manufacturer_address = db.Column(db.String())
    # link to asset
    asset_id = db.relationship("Asset", backref = "manufacturers", cascade="all, delete")
 