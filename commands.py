from main import db
from flask import Blueprint
from main import bcrypt
from models.departments import Department
from models.employees import Employee
from models.assets import Asset
from datetime import date

db_commands = Blueprint("db", __name__)

# create app's cli command named create, then run it in the terminal as "flask db create", 
# it will invoke create_db function
@db_commands .cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")


# add the data to the tables
@db_commands .cli.command("seed")
def seed_db():

    # create the department object
    department1 = Department(
        # set the attributes
        building_number = "9",
        room_number = "7",
        address = "10 Glen drive, Melbourne, Vic",
        # date = date.today()
    )
    # Add the object as a new row to the table
    db.session.add(department1)
     # This extra commit will end the transaction and generate the ids for the departments
    db.session.commit()

    # create the employee object
    employee1 = Employee(
        # set the attributes
        first_name = "Sonia",
        last_name = "Lorry",
        email_address = "S.L@asset.com",
        contact_number = "432312",
        position = "Manager",
        department_id = department1.id
        # date = date.today()
    )
    # Add the object as a new row to the table
    db.session.add(employee1)
    # This extra commit will end the transaction and generate the ids for the employee
    db.session.commit()

    # create the asset object
    asset1 = Asset(
        # set the attributes
        description = "HPLC",
        employee_id = employee1.id,
        asset_manufacturer_id = "dsfsdf"
    )

    db.session.add(asset1)

    db.session.commit()
    print("Table seeded") 

# drop all the tables
@db_commands .cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped (deleted)") 