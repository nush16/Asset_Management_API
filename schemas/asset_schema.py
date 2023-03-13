from main import ma
from schemas.employee_schema import EmployeeSchema
from marshmallow import fields

class AssetSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("id","serial_number", "date_purchased", "employee_id")
    # employee_id= fields.Nested("EmployeeSchema", only=("first_name",))

# single asset schema
asset_schema = AssetSchema()
# multiple asset schema
assets_schema = AssetSchema(many=True)