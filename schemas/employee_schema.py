from main import ma
from schemas.department_schema import DepartmentSchema
from marshmallow import fields

class EmployeeSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("id","first_name", "last_name", "email_address","contact_number","position", "department_id")
    department_id = fields.Nested(DepartmentSchema, only = ("id",))

# single employee schema
employee_schema = EmployeeSchema()
# multiple employee schema
employees_schema = EmployeeSchema(many=True)