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

@db_commands .cli.command("seed")
def seed_db():
    # create the employee object

    department1 = Department(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        building_number = "9999",
        room_number = "7777",
        address = "Ongoing",
        # date = date.today()
    )
    
    # Add the object as a new row to the table
    db.session.add(department1)
     # This extra commit will end the transaction and generate the ids for the user
    db.session.commit()

    employee1 = Employee(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        first_name = "Start the project",
        last_name = "creating the database",
        email_address = "To Do",
        contact_number = "9999",
        position = "manager",
        department_id = department1.id
        # date = date.today()
    )
    # Add the object as a new row to the table
    db.session.add(employee1)
    # This extra commit will end the transaction and generate the ids for the user
    db.session.commit()

    asset1 = Asset(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        description = "HPLC",
        employee_id = employee1.id,
        asset_manufacturer_id = "dsfsdf"
    )

    db.session.add(asset1)

    # admin_user = User(
    #     email = "admin@email.com",
    #     password = bcrypt.generate_password_hash("password123").decode("utf-8"),
    #     admin = True
    # )
    # db.session.add(admin_user)

    # user1 = User(
    #     email = "user1@email.com",
    #     password = bcrypt.generate_password_hash("123456").decode("utf-8")
    # )
    # db.session.add(user1)
    # commit the changes
    db.session.commit()
    print("Table seeded") 

@db_commands .cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 