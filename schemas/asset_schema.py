from main import ma

class AssetSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("asset_id","asset_name","serial_number", "date_purchased", "employee_id")

# single asset schema
asset_schema = AssetSchema()
# multiple asset schema
assets_schema = AssetSchema(many=True)