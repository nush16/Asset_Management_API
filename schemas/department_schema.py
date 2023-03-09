from main import ma

class DepartmentSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("id", "building_number", "room_number", "address") 

# single department schema
department_schema = DepartmentSchema()
# multiple departments schema
departments_schema = DepartmentSchema(many=True)