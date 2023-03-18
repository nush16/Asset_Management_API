from flask import Blueprint, jsonify, request, abort
from main import db
from models.employees import Employee
from models.users import User
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError, DataError
from werkzeug.exceptions import BadRequest
from schemas.employee_schema import employee_schema, employees_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

employees = Blueprint('employees', __name__, url_prefix="/employees")


# error handler for validation error in marshmallow
@employees.errorhandler(ValidationError)
def handle_validation_error(error):
    response = jsonify({'please check this field again': error.messages})
    response.status_code = 400
    return response

# The GET route endpoint - get all the employees
@employees.route("/", methods=["GET"])
def get_employees():
    # get all the employees from the database table
    employees_list = Employee.query.all()
    # Convert the employees from the database into a JSON format and store them in result
    result = employees_schema.dump(employees_list)
    # return the data in JSON format
    return jsonify(result)

# The GET routes endpoint - get details on one employee
@employees.route("/<int:id>/", methods=["GET"])
def get_employee(id):
    employee = Employee.query.get(id)
    #return an error if the employee doesn't exist
    if not employee:
        return jsonify({'error': 'Employee not found'}), 400
    # Convert the employee from the database into a JSON format and store them in result
    result = employee_schema.dump(employee)
    # return the data in JSON format
    return jsonify(result)

# The GET routes endpoint - get assets for one employee  

def employee_assets(employee_id):
    # check if employee exists
    employee = Employee.query.get(employee_id)
    # return error if employee doesnt exist
    if not employee:
        return jsonify({'error': 'Employee not found'}), 400
    # create asset dictionary
    assets_dict_list = []
    # check for all assets that belong to employee
    for asset in employee.assets:
        asset_dict = {'asset_id': asset.asset_id, 'asset_name': asset.asset_name, 'serial_number':asset.serial_number}
        # add to asset dictionary
        assets_dict_list.append(asset_dict)
    # create employee dictionary adding asset dictionary
    employee_dict = {'employee_id': employee.employee_id, 'first_name': employee.first_name, 'last_name': employee.last_name, 'assets': assets_dict_list}
    return jsonify(employee_dict)

# The GET routes endpoint - get manufacturer and assets for a employee  
@employees.route('/manufacturer/<int:employee_id>', methods=["GET"])
def employee_manufacturer(employee_id):
    # check if employee exists
    employee = Employee.query.get(employee_id)
    # return error if employee doesnt exist
    if not employee:
        return jsonify({'error': 'Employee not found'}), 400
    # create asset dictionary
    assets_dict_list = []
    # check for all assets that belong to employee
    for asset in employee.assets:
        asset_dict = {'asset_id': asset.asset_id, 'asset_name': asset.asset_name, 'serial_number':asset.serial_number}
        # add to asset dictionary
        assets_dict_list.append(asset_dict)
        # check for all manufacturers that belong to asset
        for manufacturer in asset.manufacturer_id:
                manufacturer_dict = {'manufacturer_id': manufacturer.manufacturer_id, 'manufacturer_name': manufacturer.manufacturer_name, 'manufacturer_contact_number': manufacturer.manufacturer_contact_number,'manufacturer_email': manufacturer.manufacturer_email}
                 # add to asset dictionary
                assets_dict_list.append(manufacturer_dict)
    # create employee dictionary adding asset and manufacturers
    employee_dict = {'employee_id': employee.employee_id, 'first_name': employee.first_name, 'last_name': employee.last_name, 'asset_manufacturer': assets_dict_list}
    return jsonify(employee_dict)


# The POST route endpoint - add a new employee
@employees.route("/", methods=["POST"])
@jwt_required()
def create_employees():
    # get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return jsonify({'error': 'Invalid user'}),401
    # Stop the request if the user is not an admin
    if not user.admin:
        return jsonify({'error': 'Unauthorised user'}),401
    try: 
        #Create a new employee
        employee_fields = employee_schema.load(request.json)
        new_employee = Employee()
        new_employee.first_name = employee_fields["first_name"]
        new_employee.last_name = employee_fields["last_name"]
        new_employee.email_address = employee_fields["email_address"]
        new_employee.contact_number = employee_fields["contact_number"]
        new_employee.room_number = employee_fields["room_number"]
        new_employee.position = employee_fields["position"]
        new_employee.department_id = employee_fields["department_id"]
        # not taken from the request, generated by the server
        new_employee.date = date.today()
        # add to the database and commit
        db.session.add(new_employee)
        db.session.commit()
        #return the employee in the response
        return jsonify("Employee added", employee_schema.dump(new_employee))
    except BadRequest as e:
        # Handle the case where the request data is invalid
        return jsonify({'error': str(e)}), 400
        # handle duplication of email adress and contact number
    except IntegrityError as e:
        return jsonify({'error': 'New employee could not be added, please check details again'}), 500
    except DataError as e:
        return jsonify({'error': 'Please check that correct type of data has been entered'}), 500

# The PUT route endpoint - update employee details
@employees.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_employee(id):
    # Create a new employee
    employee_fields = employee_schema.load(request.json)
    # get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return jsonify({'error': 'Invalid user'}),401
    # Stop the request if the user is not an admin
    if not user.admin:
        return jsonify({'error': 'Unauthorised user'}),401
    # find the employee
    employee = Employee.query.filter_by(employee_id=id).first()
    #return an error if the employee doesn't exist
    if not employee:
        return jsonify({'error': 'Employee does not exist'}),400
    # update the employee details with the given values
    try:
        employee.first_name = employee_fields["first_name"]
        employee.last_name = employee_fields["last_name"]
        employee.email_address = employee_fields["email_address"]
        employee.contact_number = employee_fields["contact_number"]
        employee.room_number = employee_fields["room_number"]
        employee.position = employee_fields["position"]
        employee.department_id =employee_fields["department_id"]
        # not taken from the request, generated by the server
        employee.date = date.today()
        # add to the database and commit
        db.session.commit()
        #return the employee in the response
        return jsonify("Employee updated",employee_schema.dump(employee))
    except BadRequest as e:
        # Handle the case where the request data is invalid
        return jsonify({'error': str(e)}), 400
    except IntegrityError as e:
        return jsonify({'error': 'New employee could not be added, please check details again'}), 500
    except DataError as e:
        return jsonify({'error': 'Please check that correct type of data has been entered'}), 500


# The DELETE route endpoint - delete an employee
@employees.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_employee(id):
    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return jsonify({'error': 'Invalid user'}),401
    # Stop the request if the user is not an admin
    if not user.admin:
        return jsonify({'error': 'Unauthorised user'}),401
    # find the employee
    employee = Employee.query.filter_by(employee_id=id).first()
    #return an error if the employee doesn't exist
    if not employee:
        return jsonify({'error': 'Employee does not exist'}),400
    #Delete the employee from the database and commit
    db.session.delete(employee)
    db.session.commit()
    #return the employee in the response
    return jsonify("Employee deleted", employee_schema.dump(employee))
  