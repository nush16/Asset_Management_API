from flask import Blueprint, jsonify, request
from main import db
from main import bcrypt
from main import jwt
from models.admin import Admin
from schemas.admin_schema import admin_schema
from datetime import timedelta
from flask_jwt_extended import create_access_token
from marshmallow.exceptions import ValidationError

auth = Blueprint('auth', __name__, url_prefix="/auth")

# register admin
@auth.route("/register", methods=["POST"])
def auth_register():
    #The request data will be loaded in a user_schema converted to JSON. request needs to be imported from
    admin_fields = admin_schema.load(request.json)
    #Create the user object
    admin = Admin()
    #Add the email attribute
    admin.email = admin_fields["email"]
    #Add the password attribute hashed by bcrypt
    admin.password = bcrypt.generate_password_hash(admin_fields["password"]).decode("utf-8")
    #Add it to the database and commit the changes
    db.session.add(admin)
    db.session.commit()
    #Return the user to check the request was successful
    return jsonify(admin_schema.dump(admin))


#Login admin POST
@auth.route("/login",methods = ["POST"])
def login_admin():
    # Get username and password fron the request
    admin_fields = admin_schema.load(request.json)
    # Check username and password. admin needs to exist, and password needs to match
    admin = Admin.query.filter_by(email=admin_fields["email"]).first()
    if not admin:
        return {"error": "email is not valid"}
    
    if not bcrypt.check_password_hash(admin.password, admin_fields["password"]):
        return {"error": "wrong password"}
    # Credentials are valid, so generate token and return it to the user

    token = create_access_token(identity="admin", expires_delta=timedelta(days=1)) 

    return {"admin": admin.email, "token": token}

# @auth.errorhandler(ValidationError)
# def register_validation_error(error):
#     #print(error.messages)
#     return error.messages, 400