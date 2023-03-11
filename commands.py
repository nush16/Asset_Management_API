from main import db
from flask import Blueprint
from main import bcrypt
from models.departments import Department
from models.employees import Employee
from models.assets import Asset
from models.asset_type import AssetType
# from models.manufacturer import Manufacturer
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
        department_name = "A",
        building_number = "1",
        address = "10 Glen drive, Melbourne, VIC",
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
        room_number = "15",
        position = "Manager",
        department_id = department1.id
        # date = date.today()
    )
    # Add the object as a new row to the table
    db.session.add(employee1)
    # This extra commit will end the transaction and generate the ids for the employee
    db.session.commit()

    asset1 = Asset(
        # set the attributes
        serial_number = "a3546",
        date_purchased = "jghh",
        # asset_type_id = department1.id,
        employee_id = employee1.id,
    )

    db.session.add(asset1)
    db.session.commit()

    asset_type1 = AssetType(
        # set the attributes
        description = "akkkkk",
        asset_id = asset1.id,
        # manufacturer_id = employee1.id,
    )

    db.session.add(asset_type1)
    db.session.commit()
    # create the asset object
# create the asset object
   
    # create the asset object
    # manfacturer1 = Manufacturer(
    #     # set the attributes
    #     manufacturer_name = "Thermo",
    #     manufacturer_contact_number = "11111",
    #     manufacturer_email = "thermo@email.com",
    #     manufacturer_address = "1 Tree Road, Sydney, NSW",
    #     asset_id = asset1.id
    # )

    # manfacturer2 = Manufacturer(
    #     # set the attributes
    #     manufacturer_name = "Agilent",
    #     manufacturer_contact_number = "22222",
    #     manufacturer_email = "agilent@email.com",
    #     manufacturer_address = "2 Tree Road, Sydney, NSW",
    #     asset_id = asset1.id
    # )

    # manfacturer3 = Manufacturer(
    #     # set the attributes
    #     manufacturer_name = "Shimadzu",
    #     manufacturer_contact_number = "33333",
    #     manufacturer_email = "agilent@email.com",
    #     manufacturer_address = "3 Tree Road, Sydney, NSW",
    #     asset_id = asset1.id
    # )

    # manfacturer4 = Manufacturer(
    #     # set the attributes
    #     manufacturer_name = "PE",
    #     manufacturer_contact_number = "44444",
    #     manufacturer_email = "pe@email.com",
    #     manufacturer_address = "4 Tree Road, Sydney, NSW",
    #     asset_id = asset1.id
    # )

    # manfacturer5 = Manufacturer(
    #     # set the attributes
    #     manufacturer_name = "Bruker",
    #     manufacturer_contact_number = "55555",
    #     manufacturer_email = "bruker@email.com",
    #     manufacturer_address = "5 Tree Road, Sydney, NSW",
    #     asset_id = asset1.id
    # )

    # db.session.add(manfacturer1)
    # db.session.add(manfacturer1, manfacturer2, manfacturer3, manfacturer4, manfacturer5)

    db.session.commit()
    print("Tables seeded (added)") 

# drop all the tables
@db_commands .cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped (deleted)") 