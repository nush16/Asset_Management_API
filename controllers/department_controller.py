from flask import Blueprint, jsonify, request, abort
from main import db
from models.departments import Department
from models.admin import Admin
from schemas.department_schema import department_schema, departments_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

departments = Blueprint('departments', __name__ , url_prefix="/departments")

# The GET route endpoint - get all the departments
@departments.route("/", methods=["GET"])
def get_departments():
    # get all the departments from the database table
    departments_list = Department.query.all()
    # # Convert the departments from the database into a JSON format and store them in result
    result = departments_schema.dump(departments_list)
    # return the data in JSON format
    # return jsonify(result)
    return jsonify(result)

# The GET manufacturer routes endpoint - get details on one customer
@departments.route("/<int:id>/", methods=["GET"])
def get_department(id):
    department = Department.query.get(id)
    #return an error if the card doesn't exist
    if not department:
        return abort(400, description= "department does not exist")
    # Convert the cards from the database into a JSON format and store them in result
    result = department_schema.dump(department)
    # return the data in JSON format
    return jsonify(result)


# The POST route endpoint - add a department
@departments.route("/", methods=["POST"])
@jwt_required()
def create_department():
    # #Create a new department
    department_fields = department_schema.load(request.json)

    new_department = Department()
    new_department.department_name = department_fields["department_name"]
    new_department.building_number = department_fields["building_number"]
    new_department.address = department_fields["address"]
    # not taken from the request, generated by the server
    new_department.date = date.today()
    # add to the database and commit
    db.session.add(new_department)
    db.session.commit()
    #return the department in the response
    return jsonify(department_schema.dump(new_department))

# The PUT route endpoint - update department details
@departments.route("/<int:id>/", methods=["PUT"])
# @jwt_required()
def update_department(id):
    # #Create a new card
    department_fields = department_schema.load(request.json)

    #get the user id invoking get_jwt_identity
    # user_id = get_jwt_identity()
    #Find it in the db
    # user = User.query.get(user_id)
    # #Make sure it is in the database
    # if not user:
    #     return abort(401, description="Invalid user")
    # # Stop the request if the user is not an admin
    # if not user.admin:
    #     return abort(401, description="Unauthorised user")
    # # find the card
    department = Department.query.filter_by(id=id).first()
    # #return an error if the card doesn't exist
    # if not card:
    #     return abort(400, description= "Card does not exist")
    #update the car details with the given values
    department.department_name = department_fields["department_name"]
    department.building_number = department_fields["building_number"]
    department.address = department_fields["address"]
    # not taken from the request, generated by the server
    department.date = date.today()
    # add to the database and commit
    db.session.commit()
    #return the card in the response
    return jsonify(department_schema.dump(department))



# The DELETE route endpoint - delete a department
@departments.route("/<int:id>/", methods=["DELETE"])
# @jwt_required()
def delete_department(id):
    #get the admin id invoking get_jwt_identity
    # admin_id = get_jwt_identity()
    # #Find it in the db
    # admin = Admin.query.get(admin_id)
    # #Make sure it is in the database
    # if not admin:
    #     return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
    # if not admin.admin:
    #     return abort(401, description="Unauthorised user")
    # find the department
    department = Department.query.filter_by(id=id).first()
    #return an error if the department doesn't exist
    if not department:
        return abort(400, description= "department doesn't exist")
    #Delete the department from the database and commit
    db.session.delete(department)
    db.session.commit()
    #return the card in the response
    return jsonify(department_schema.dump(department))
   