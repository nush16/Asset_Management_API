from main import db
from flask import Blueprint
from main import bcrypt
from models.departments import Department
from models.employees import Employee
# from models.users import User
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
    # employee1 = Employee(
    #     # set the attributes, not the id, SQLAlchemy will manage that for us
    #     first_name = "Start the project",
    #     last_name = "Stage 1, creating the database",
    #     email_address = "To Do",
    #     contact_number = "9999",
    #     position = "manager",
    #     # date = date.today()
    # )
    # # Add the object as a new row to the table
    # db.session.add(employee1)

    department1 = Department(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        building_number = "9999",
        room_number = "7777",
        address = "Ongoing",
        # date = date.today()
    )
    # Add the object as a new row to the table
    db.session.add(department1)


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