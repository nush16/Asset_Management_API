from main import ma

class EmployeeSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("employee_id", "first_name", "last_name", "email_address", "contact_number", "room_number", "position", "department_id")

# single employee schema
employee_schema = EmployeeSchema()
# multiple employee schema
employees_schema = EmployeeSchema(many=True)