from main import ma
from marshmallow.validate import Length

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "password")
    #password's length to a minimum of 6 characters
    password = ma.String(validate=Length(min=6))

# single user schema
user_schema = UserSchema()
