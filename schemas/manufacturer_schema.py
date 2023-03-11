from main import ma
from marshmallow import fields
# from schemas.asset_schema import AssetSchema

class ManufacturerSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("id", "name", "manufacturer_contact_number", "manufacturer_email", "manufacturer_address", "asset_id") 
    # asset_id = fields.Nested(AssetSchema, only = ("id",))

# single asset manufacturer schema
manufacturer_schema = ManufacturerSchema()
# multiple asset manufacturer schema
manufacturers_schema = ManufacturerSchema(many=True)