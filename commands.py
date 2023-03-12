from main import db
from flask import Blueprint
from main import bcrypt
from models.departments import Department
from models.employees import Employee
from models.assets import Asset
from models.asset_type import AssetType
from models.manufacturer import Manufacturer


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
    )
    # Add the object as a new row to the table
    db.session.add(department1)


    # create the department object
    department2 = Department(
        # set the attributes
        department_name = "B",
        building_number = "2",
        address = "11 Glen drive, Melbourne, VIC", 
    )
    # Add the object as a new row to the table
    db.session.add(department2)

    # create the department object
    department3 = Department(
        # set the attributes
        department_name = "C",
        building_number = "3",
        address = "12 Glen drive, Melbourne, VIC",
    )
    # Add the object as a new row to the table
    db.session.add(department3)

     # This extra commit will end the transaction and generate the ids for the departments
    db.session.commit()

    # create the employee object
    employee1 = Employee(
        # set the attributes
        first_name = "Sonia",
        last_name = "Lorry",
        email_address = "S.L@asset.com",
        contact_number = "432311",
        room_number = "15",
        position = "Manager",
        department_id = department1.id
    )
    # Add the object as a new row to the table
    db.session.add(employee1)

    employee2 = Employee(
        # set the attributes
        first_name = "Jim",
        last_name = "Tucker",
        email_address = "J.T@asset.com",
        contact_number = "432312",
        room_number = "7",
        position = "Supervisor",
        department_id = department3.id
    
    )
    # Add the object as a new row to the table
    db.session.add(employee2)


    employee3 = Employee(
        # set the attributes
        first_name = "Sally",
        last_name = "Robertson",
        email_address = "S.R@asset.com",
        contact_number = "432313",
        room_number = "6",
        position = "Scientist",
        department_id = department3.id
    
    )
    # Add the object as a new row to the table
    db.session.add(employee3)

    employee4 = Employee(
        # set the attributes
        first_name = "Kerry",
        last_name = "Lam",
        email_address = "K.L@asset.com",
        contact_number = "432314",
        room_number = "5",
        position = "Manager",
        department_id = department2.id
    
    )
    # Add the object as a new row to the table
    db.session.add(employee4)

    employee5 = Employee(
        # set the attributes
        first_name = "Jessica",
        last_name = "Lee",
        email_address = "J.L@asset.com",
        contact_number = "432315",
        room_number = "8",
        position = "Scientist",
        department_id = department1.id
    
    )
    # Add the object as a new row to the table
    db.session.add(employee5)

    # This extra commit will end the transaction and generate the ids for the employee
    db.session.commit()

    # create the asset object
    asset1 = Asset(
        # set the attributes
        serial_number = "a3546",
        date_purchased = "jghh",
        employee_id = employee1.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset1)

    # create the asset object
    asset2 = Asset(
        # set the attributes
        serial_number = "r3547",
        date_purchased = "jghh",
        employee_id = employee1.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset2)

    # create the asset object
    asset3 = Asset(
        # set the attributes
        serial_number = "a3548",
        date_purchased = "jghh",
        employee_id = employee2.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset3)

    # create the asset object
    asset4 = Asset(
        # set the attributes
        serial_number = "e3558",
        date_purchased = "jghh",
        employee_id = employee2.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset4)

    # create the asset object
    asset5 = Asset(
        # set the attributes
        serial_number = "w3559",
        date_purchased = "jghh",
        employee_id = employee3.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset5)

    # create the asset object
    asset6 = Asset(
        # set the attributes
        serial_number = "z3579",
        date_purchased = "jghh",
        employee_id = employee3.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset6)

    # create the asset object
    asset7 = Asset(
        # set the attributes
        serial_number = "b3479",
        date_purchased = "jghh",
        employee_id = employee4.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset7)

    # create the asset object
    asset8 = Asset(
        # set the attributes
        serial_number = "y3499",
        date_purchased = "jghh",
        employee_id = employee4.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset8)

    # create the asset object
    asset9 = Asset(
        # set the attributes
        serial_number = "p3779",
        date_purchased = "jghh",
        employee_id = employee4.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset9)

    # create the asset object
    asset10 = Asset(
        # set the attributes
        serial_number = "w8789",
        date_purchased = "jghh",
        employee_id = employee5.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset10)

    # create the asset object
    asset11 = Asset(
        # set the attributes
        serial_number = "o8u89",
        date_purchased = "jghh",
        employee_id = employee5.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset11)

    # create the asset object
    asset12 = Asset(
        # set the attributes
        serial_number = "w87rp",
        date_purchased = "jghh",
        employee_id = employee5.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset12)

    # create the asset object
    asset13 = Asset(
        # set the attributes
        serial_number = "w8oh9",
        date_purchased = "jghh",
        employee_id = employee5.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset13)

    # This extra commit will end the transaction and generate the ids for the assets
    db.session.commit()

    # create the asset_type object
    asset_type1 = AssetType(
        # set the attributes
        description = "HPLC",
        asset_id = asset1.id, 
    )
    # Add the object as a new row to the table
    db.session.add(asset_type1)

    # create the asset_type object
    asset_type2 = AssetType(
        # set the attributes
        description = "HPLC",
        asset_id = asset2.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type2)

    # create the asset_type object
    asset_type3 = AssetType(
        # set the attributes
        description = "GCMS",
        asset_id = asset2.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type3)

     # create the asset_type object
    asset_type4 = AssetType(
        # set the attributes
        description = "FTIR",
        asset_id = asset4.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type4)

    # create the asset_type object
    asset_type5 = AssetType(
        # set the attributes
        description = "IC",
        asset_id = asset5.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type5)

    # create the asset_type object
    asset_type6 = AssetType(
        # set the attributes
        description = "LCMS",
        asset_id = asset6.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type6)

    # create the asset_type object
    asset_type7 = AssetType(
        # set the attributes
        description = "LCMS",
        asset_id = asset7.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type7)

    # create the asset object
    asset_type8 = AssetType(
        # set the attributes
        description = "GCMS",
        asset_id = asset8.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type8)

    # create the asset object
    asset_type9 = AssetType(
        # set the attributes
        description = "GCMS",
        asset_id = asset9.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type9)

    # create the asset object
    asset_type10 = AssetType(
        # set the attributes
        description = "GCMS",
        asset_id = asset10.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type10)

    # create the asset object
    asset_type11 = AssetType(
        # set the attributes
        description = "HPLC",
        asset_id = asset11.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type11)

    # create the asset object
    asset_type12 = AssetType(
        # set the attributes
        description = "HPLC",
        asset_id = asset12.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type12)

    # create the asset object
    asset_type13 = AssetType(
        # set the attributes
        description = "FTIR",
        asset_id = asset13.id,
    )
    # Add the object as a new row to the table
    db.session.add(asset_type13)

    # This extra commit will end the transaction and generate the ids for the asset_types
    db.session.commit()
   
    # create the asset object
    manfacturer1 = Manufacturer(
        # set the attributes
        manufacturer_name = "Thermo",
        manufacturer_contact_number = "111",
        manufacturer_email = "thermo@email.com",
        manufacturer_address = "1 Tree Road, Sydney, NSW",
        asset_type_id = asset_type1.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer1)

    # create the asset object
    manfacturer2 = Manufacturer(
        # set the attributes
        manufacturer_name = "Agilent",
        manufacturer_contact_number = "22222",
        manufacturer_email = "agilent@email.com",
        manufacturer_address = "2 Tree Road, Sydney, NSW",
        asset_type_id = asset_type2.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer2)

    # create the asset object
    manfacturer3 = Manufacturer(
        # set the attributes
        manufacturer_name = "Agilent",
        manufacturer_contact_number = "22222",
        manufacturer_email = "agilent@email.com",
        manufacturer_address = "2 Tree Road, Sydney, NSW",
        asset_type_id = asset_type3.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer3)

    # create the asset object
    manfacturer4 = Manufacturer(
        # set the attributes
        manufacturer_name = "Thermo",
        manufacturer_contact_number = "111",
        manufacturer_email = "thermo@email.com",
        manufacturer_address = "1 Tree Road, Sydney, NSW",
        asset_type_id = asset_type4.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer4)

     # create the asset object
    manfacturer5 = Manufacturer(
        # set the attributes
        manufacturer_name = "Thermo",
        manufacturer_contact_number = "111",
        manufacturer_email = "thermo@email.com",
        manufacturer_address = "1 Tree Road, Sydney, NSW",
        asset_type_id = asset_type5.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer5)
    
    # create the asset object
    manfacturer6 = Manufacturer(
        # set the attributes
        manufacturer_name = "Bruker",
        manufacturer_contact_number = "55555",
        manufacturer_email = "bruker@email.com",
        manufacturer_address = "5 Tree Road, Sydney, NSW",
        asset_type_id = asset_type6.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer6)
    
    # create the asset object
    manfacturer7 = Manufacturer(
        # set the attributes
        manufacturer_name = "Shimadzu",
        manufacturer_contact_number = "33333",
        manufacturer_email = "agilent@email.com",
        manufacturer_address = "3 Tree Road, Sydney, NSW",
        asset_type_id = asset_type7.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer7)

    # create the asset object
    manfacturer8 = Manufacturer(
        # set the attributes
        manufacturer_name = "Thermo",
        manufacturer_contact_number = "111",
        manufacturer_email = "thermo@email.com",
        manufacturer_address = "1 Tree Road, Sydney, NSW",
        asset_type_id = asset_type8.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer8)

    # create the asset object
    manfacturer9 = Manufacturer(
        # set the attributes
        manufacturer_name = "PE",
        manufacturer_contact_number = "44444",
        manufacturer_email = "pe@email.com",
        manufacturer_address = "4 Tree Road, Sydney, NSW",
        asset_type_id = asset_type9.id
    )
     # Add the object as a new row to the table
    db.session.add(manfacturer9)

    # create the asset object
    manfacturer10 = Manufacturer(
        # set the attributes
        manufacturer_name = "Agilent",
        manufacturer_contact_number = "22222",
        manufacturer_email = "agilent@email.com",
        manufacturer_address = "2 Tree Road, Sydney, NSW",
        asset_type_id = asset_type10.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer10)

    # create the asset object
    manfacturer11 = Manufacturer(
        # set the attributes
        manufacturer_name = "Bruker",
        manufacturer_contact_number = "55555",
        manufacturer_email = "bruker@email.com",
        manufacturer_address = "5 Tree Road, Sydney, NSW",
        asset_type_id = asset_type11.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer11)

    # create the asset object
    manfacturer12 = Manufacturer(
        # set the attributes
        manufacturer_name = "Shimadzu",
        manufacturer_contact_number = "33333",
        manufacturer_email = "agilent@email.com",
        manufacturer_address = "3 Tree Road, Sydney, NSW",
        asset_type_id = asset_type12.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer12)

    # create the asset object
    manfacturer13 = Manufacturer(
        # set the attributes
        manufacturer_name = "Thermo",
        manufacturer_contact_number = "111",
        manufacturer_email = "thermo@email.com",
        manufacturer_address = "1 Tree Road, Sydney, NSW",
        asset_type_id = asset_type13.id
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer13)

    db.session.commit()
    print("Tables seeded (added)") 

# drop all the tables
@db_commands .cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped (deleted)") 