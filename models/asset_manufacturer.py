from main import db

class asset_manufacturer(db.Model):
    # define the table name for the db as asset_manufacturers
    __tablename__= "Asset_Manufacturers"
    # Set the primary key
    id = db.Column(db.Integer,primary_key=True)
    # the rest of the attributes/columns
    manufacturer_contact_number = db.Column(db.Integer())
    manufacturer_email = db.Column(db.Varchar())
    manufacturer_address = db.Column(db.String())
    asset_id = db.Column(db.String())