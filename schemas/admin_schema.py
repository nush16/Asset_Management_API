from main import ma
from marshmallow.validate import Length

class AdminSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "password")
    #add validation to password
    password = ma.String(validate=Length(min=6))

#just the single schema for log in purposes
admin_schema = AdminSchema()