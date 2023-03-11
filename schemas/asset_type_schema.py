from main import ma
from schemas.asset_schema import AssetSchema
from marshmallow import fields

class AssetTypeSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("id","asset_id", "description")
    asset_id = fields.Nested(AssetSchema, only = ("id",))

# single asset schema
asset_type_schema = AssetTypeSchema()
# multiple asset schema
asset_types_schema = AssetTypeSchema(many=True)