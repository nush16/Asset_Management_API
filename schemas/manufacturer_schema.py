from main import ma

class ManufacturerSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("manufacturer_id", "manufacturer_name", "manufacturer_contact_number", "manufacturer_email", "manufacturer_address", "asset_id") 


# single asset manufacturer schema
manufacturer_schema = ManufacturerSchema()
# multiple asset manufacturer schema
manufacturers_schema = ManufacturerSchema(many=True)