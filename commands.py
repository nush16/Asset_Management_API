from main import db
from flask import Blueprint
from main import bcrypt
from models.users import User
from models.departments import Department
from models.employees import Employee
from models.assets import Asset
from models.service_job import ServiceJob
from models.manufacturer import Manufacturer
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

    admin_user = User(
        email = "admin@email.com",
        password = bcrypt.generate_password_hash("password123").decode("utf-8"),
        admin = True
    )
    db.session.add(admin_user)

    user1 = User(
        email = "user1@email.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )
    db.session.add(user1)
    # commit the changes
    db.session.commit()

    # create the department object
    department1 = Department(
        # set the attributes
        department_name = "A",
        building_number = "6",
        address = "10 Glen drive, Melbourne, VIC",
    )
    # Add the object as a new row to the table
    db.session.add(department1)


    # create the department object
    department2 = Department(
        # set the attributes
        department_name = "B",
        building_number = "7",
        address = "11 Glen drive, Melbourne, VIC", 
    )
    # Add the object as a new row to the table
    db.session.add(department2)

    # create the department object
    department3 = Department(
        # set the attributes
        department_name = "C",
        building_number = "8",
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
        department_id = department1.department_id
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
        department_id = department3.department_id
    
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
        department_id = department3.department_id
    
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
        department_id = department2.department_id
    
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
        department_id = department1.department_id
    
    )
    # Add the object as a new row to the table
    db.session.add(employee5)

    # This extra commit will end the transaction and generate the ids for the employee
    db.session.commit()

    # create the asset object
    asset1 = Asset(
        # set the attributes
        asset_name = "Vanquish",
        serial_number = "a3546",
        date_purchased = date(day = 15, month = 3,year = 2009),
        employee_id = employee1.employee_id
    )
    # Add the object as a new row to the table
    db.session.add(asset1)

    # create the asset object
    asset2 = Asset(
        # set the attributes
        asset_name = "Infinity",
        serial_number = "r3547",
        date_purchased = date(day = 8, month = 7,year = 2020),
        employee_id = employee1.employee_id
    )
    # Add the object as a new row to the table
    db.session.add(asset2)

    # create the asset object
    asset3 = Asset(
        # set the attributes
        asset_name = "7000E",
        serial_number = "a3548",
        date_purchased = date(day = 9, month = 4,year = 2021),
        employee_id = employee2.employee_id
    )
    # Add the object as a new row to the table
    db.session.add(asset3)

    # create the asset object
    asset4 = Asset(
        # set the attributes
        asset_name = "iS10",
        serial_number = "e3558",
        date_purchased = date(day = 20, month = 9,year = 2015),
        employee_id = employee2.employee_id
    )
    # Add the object as a new row to the table
    db.session.add(asset4)

    # create the asset object
    asset5 = Asset(
        # set the attributes
        asset_name = "Aquion",
        serial_number = "w3559",
        date_purchased = date(day = 7, month = 7,year = 2017),
        employee_id = employee3.employee_id
    )
    # Add the object as a new row to the table
    db.session.add(asset5)

    # create the asset object
    asset6 = Asset(
        # set the attributes
        asset_name = "Maldi",
        serial_number = "z3579",
        date_purchased = date(day = 8, month = 7,year = 2013),
        employee_id = employee3.employee_id
    )
    # Add the object as a new row to the table
    db.session.add(asset6)

    # create the asset object
    asset7 = Asset(
        # set the attributes
        asset_name = "8060NX",
        serial_number = "b3479",
        date_purchased = date(day = 15, month = 4,year = 2022),
        employee_id = employee4.employee_id
    )
    # Add the object as a new row to the table
    db.session.add(asset7)

    # create the asset object
    asset8 = Asset(
        # set the attributes
        asset_name = "TSQ8000",
        serial_number = "y3499",
        date_purchased = date(day = 9, month = 6,year = 2018),
        employee_id = employee4.employee_id
    )
    # Add the object as a new row to the table
    db.session.add(asset8)

    # create the asset object
    asset9 = Asset(
        # set the attributes
        asset_name = "PEGCMS",
        serial_number = "p3779",
        date_purchased = date(day = 15, month = 11,year = 2013),
        employee_id = employee4.employee_id,
    )
    # Add the object as a new row to the table
    db.session.add(asset9)

    # create the asset object
    asset10 = Asset(
        # set the attributes
        asset_name = "7000E",
        serial_number = "w8789",
        date_purchased = date(day = 30, month = 6,year = 2016),
        employee_id = employee5.employee_id,
    )
    # Add the object as a new row to the table
    db.session.add(asset10)

    # create the asset object
    asset11 = Asset(
        # set the attributes
        asset_name = "Elute",
        serial_number = "o8u89",
        date_purchased = date(day = 5, month = 9,year = 2022),
        employee_id = employee5.employee_id
    )
    # Add the object as a new row to the table
    db.session.add(asset11)

    # create the asset object
    asset12 = Asset(
        # set the attributes
        asset_name = "LC-2030C",
        serial_number = "w87rp",
        date_purchased = date(day = 25, month = 8,year = 2019),
        employee_id = employee5.employee_id
    )
    # Add the object as a new row to the table
    db.session.add(asset12)

    # create the asset object
    asset13 = Asset(
        # set the attributes
        asset_name = "iS50",
        serial_number = "w8oh9",
        date_purchased = date(day = 1, month = 8,year = 2014),
        employee_id = employee5.employee_id
    )
    # Add the object as a new row to the table
    db.session.add(asset13)

    # This extra commit will end the transaction and generate the ids for the assets
    db.session.commit()

    # create the asset_type object
    service_job1 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 1, month = 6,year = 2021),
        asset_id = asset1.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job1)

    # create the asset_type object
    service_job2 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 1, month = 8,year = 2022),
        asset_id = asset1.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job2)

    # create the asset_type object
    service_job3 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 5, month = 5,year = 2017),
        asset_id = asset1.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job3)

     # create the asset_type object
    # create the asset_type object
    service_job4 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 1, month = 8,year = 2021),
        asset_id = asset2.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job4)

    # create the asset_type object
    service_job5 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 5, month = 8,year = 2022),
        asset_id = asset2.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job5)

    # create the asset_type object
    service_job6 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 1, month = 4,year = 2021),
        asset_id = asset3.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job6)

    # create the asset_type object
    service_job7 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 1, month = 8,year = 2022),
        asset_id = asset3.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job7)

    # create the asset_type object
    service_job8 = ServiceJob(
        # set the attributes
        service_description = "Repair",
        service_date = date(day = 9, month = 8,year = 2021),
        asset_id = asset4.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job8)

    # create the asset_type object
    service_job9 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 24, month = 8,year = 2021),
        asset_id = asset4.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job9)

    # create the asset_type object
    service_job10 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 5, month = 8,year = 2022),
        asset_id = asset5.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job10)

    # create the asset_type object
    service_job11 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 21, month = 8,year = 2021),
        asset_id = asset5.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job11)

    # create the asset_type object
    service_job12 = ServiceJob(
        # set the attributes
        service_description = "Repair",
        service_date = date(day = 1, month = 5,year = 2022),
        asset_id = asset6.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job12)

    # create the asset_type object
    service_job13 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 1, month = 1,year = 2023),
        asset_id = asset6.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job13)

    # create the asset_type object
    service_job14 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 1, month = 4,year = 2022),
        asset_id = asset6.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job14)

    # create the asset_type object
    service_job15 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 11, month = 9,year = 2021),
        asset_id = asset7.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job15)

    # create the asset_type object
    service_job16 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 1, month = 4,year = 2022),
        asset_id = asset7.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job16)

    # create the asset_type object
    service_job17 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 1, month = 4,year = 2021),
        asset_id = asset8.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job17)

    # create the asset_type object
    service_job18 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 1, month = 3,year = 2023),
        asset_id = asset8.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job18)

    # create the asset_type object
    service_job19 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 1, month = 5,year = 2021),
        asset_id = asset9.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job19)

    # create the asset_type object
    service_job20 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 1, month = 3,year = 2020),
        asset_id = asset9.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job20)

    # create the asset_type object
    service_job21 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 12, month = 9,year = 2022),
        asset_id = asset9.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job21)

     # create the asset_type object
    service_job22 = ServiceJob(
        # set the attributes
        service_description = "Repair",
        service_date = date(day = 12, month = 1,year = 2023),
        asset_id = asset10.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job22)

     # create the asset_type object
    service_job23 = ServiceJob(
        # set the attributes
        service_description = "Repair",
        service_date = date(day = 12, month = 11,year = 2022),
        asset_id = asset10.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job23)

     # create the asset_type object
    service_job24 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 5, month = 10,year = 2021),
        asset_id = asset10.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job24)

      # create the asset_type object
    service_job25 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 8, month = 12,year = 2022),
        asset_id = asset11.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job25)

     # create the asset_type object
    service_job26 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 6, month = 7,year = 2021),
        asset_id = asset11.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job26)

     # create the asset_type object
    service_job27 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 8, month = 1,year = 2022),
        asset_id = asset12.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job27)

     # create the asset_type object
    service_job28 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 18, month = 10,year = 2021),
        asset_id = asset12.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job28)

      # create the asset_type object
    service_job29 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 18, month = 10,year = 2023),
        asset_id = asset12.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job29)

      # create the asset_type object
    service_job30 = ServiceJob(
        # set the attributes
        service_description = "PM",
        service_date = date(day = 8, month = 1,year = 2022),
        asset_id = asset13.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job30)

      # create the asset_type object
    service_job31 = ServiceJob(
        # set the attributes
        service_description = "Qualification",
        service_date = date(day = 8, month = 1,year = 2023),
        asset_id = asset13.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(service_job31)


    # This extra commit will end the transaction and generate the ids for the asset_types
    db.session.commit()
   
    # create the asset object
    manfacturer1 = Manufacturer(
        # set the attributes
        manufacturer_name = "Thermo",
        manufacturer_contact_number = "111",
        manufacturer_email = "thermo@email.com",
        manufacturer_address = "1 Tree Road, Sydney, NSW",
        asset_id = asset1.asset_id 
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
        asset_id = asset2.asset_id 
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
        asset_id = asset3.asset_id 
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
        asset_id = asset4.asset_id 
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
        asset_id = asset5.asset_id 
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
        asset_id = asset6.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer6)
    
    # create the asset object
    manfacturer7 = Manufacturer(
        # set the attributes
        manufacturer_name = "Shimadzu",
        manufacturer_contact_number = "33333",
        manufacturer_email = "shimadzu@email.com",
        manufacturer_address = "3 Tree Road, Sydney, NSW",
        asset_id = asset7.asset_id 
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
        asset_id = asset8.asset_id 
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
        asset_id = asset9.asset_id 
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
        asset_id = asset10.asset_id 
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
        asset_id = asset11.asset_id 
    )
    # Add the object as a new row to the table
    db.session.add(manfacturer11)

    # create the asset object
    manfacturer12 = Manufacturer(
        # set the attributes
        manufacturer_name = "Shimadzu",
        manufacturer_contact_number = "33333",
        manufacturer_email = "shimadzu@email.com",
        manufacturer_address = "3 Tree Road, Sydney, NSW",
        asset_id = asset12.asset_id 
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
        asset_id = asset13.asset_id 
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