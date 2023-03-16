from main import ma

class AssetTypeSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("asset_type_id","asset_id", "description")

# single asset schema
asset_type_schema = AssetTypeSchema()
# multiple asset schema
asset_types_schema = AssetTypeSchema(many=True)