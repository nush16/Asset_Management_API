from main import ma

class EmployeeSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("first_name", "last_name", "email_address","contact_number","position") 

# single employee schema
employee_schema = EmployeeSchema()
# multiple employee schema
employees_schema = EmployeeSchema(many=True)