from main import ma
from marshmallow import fields
from schemas.asset_type_schema import AssetTypeSchema


class ManufacturerSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("id", "manufacturer_name", "manufacturer_contact_number", "manufacturer_email", "manufacturer_address", "asset_type_id") 
    asset_type_id = fields.Nested(AssetTypeSchema, only = ("id",))

# single asset manufacturer schema
manufacturer_schema = ManufacturerSchema()
# multiple asset manufacturer schema
manufacturers_schema = ManufacturerSchema(many=True)