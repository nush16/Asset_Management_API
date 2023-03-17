# *Lab Asset Management API*

## *Identification of the problem you are trying to solve by building this particular app.*
I came accross this problem in real life where I was helping a customer in relocating some of there labratory instruments from one site to a newly built site. Ths customer is a massive organisation that has many instruments, employees and departments and had trouble in identifying:
* what instuments each department have
* who the main contact for the instrument is
* who the manufacturer of the instrument is
* what the serial number of the instrument is 
* what type is instrument (could other manufacturers relocate) 

They were dealing with over 600 manfacturers (Internationally and locally) and spent over a year trying to get this data. The API I have created (even though on a simplier scale) was designed to address and rectify all these issues in indentifying where lab instruments could belong.

## *Why is it a problem that needs solving?*
asset management is 




## *Why have you chosen this database system. What are the drawbacks compared to others?*






## *Identify and discuss the key functionalities and benefits of an ORM*



## *Document all endpoints for your API*

- Get all employees
- Get all assets
- Get all manufacturers
- Get all departments
- Get all assets in a department
- Get assets a employee could have
- Get all manufacturers assets a department has

- Delete employee
- Delete asset
- Delete department
- Delete manufacturer 

- Add employee
- Add asset
- Add manufacturer
- Add department

- Update employee
- Update asset
- Update manufacturer
- Update department


## *An ERD for your app*
Please see the below for the ERD.


## *Detail any third party services that your app will use*

Bcrypt

Marshmallow


## *Describe your projects models in terms of the relationships they have with each other*

### Department and Employees -
This is a one to many relationship. A employee can only belong to one department, while one department can have many employees. 

### Employees and Assets-
This is a one to many relationship. A employee can have many assets, while only one asset can only belong to employee

### Assets and Manufacturers
This is a one to many relationship. A asset only be manufactured by only one manufacturer while one manufacturer can manufacturer many different types of assets

### Users
This is model only has access to the data in the tables and has no relationship in the ERD. Only with admin privliges can a user insert, update and delete data in the tables. A standard user can only view data in the tables

## *Discuss the database relations to be implemented in your application*






## *Describe the way tasks are allocated and tracked in your project*
These were the steps I used to track and visualise my project
1. Decide on a idea for project
2. Visualise the data and fields in excel (haha yes i know excel) - this would help me build the ERD and build the models. It looked like the below.









3. Build the ERD and identify the relationships between each model
4. Start tracking on trello - please click here
5. After creating all the files and linking to the database, created all the models
6. all the schemas were next created
7. Controllers with 'GET' command were next created - this is so i could test if the database and relationships were working as intended in step 9.
8. Data to be seeded to the tables - this was so i could
9. Testing 
10. Built a 'user' model so i could add admin prvileges for a user to update, insert and delete data in the tables. also build a schema and added this to the 'auth' controller
11. added 'PUT', 'POST' and 'DELETE' to the controller.
12. Testing - document this 

## *admin privileges*

- add, delete and update employees
- add, delete and update manufacturers
- add, delete and update departments
- add, delete and update assets
  

