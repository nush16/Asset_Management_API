# *Lab Asset Management API*

## *Installation*

### Requirements
Have PostgreSQL installed

### 1. create and active a vitual environment
```virtualenv venv && source venv/bin/activate```

### 2. Installing dependencies
```pip install -r ./src/requirements.txt```

### 3. Create database
```flask db create```

### 4. Seed database - using data already provided
```flask db seed```

### 5. Drop database - remove data and tables
```flask db drop```

## *Identification of the problem you are trying to solve by building this particular app.*
I came accross this problem in real life where I was helping a customer in relocating some of there labratory instruments from one site to a newly built site. Ths customer is a massive organisation that has many instruments, employees and departments and had trouble in identifying:
* what instuments each department have
* who the main contact for the instrument is
* who the manufacturer of the instrument is
* what the serial number of the instrument is 
* what type is instrument (could other manufacturers relocate) 
* when was the last PM/qualification for the instrument - will a service need to be done when relocated

They were dealing with over 600 manfacturers (Internationally and locally) and spent over a year trying to get this data. The API I have created (even though on a simplier scale) was designed to address and rectify all these issues in indentifying where lab instruments could belong. 

## *Why is it a problem that needs solving?*
lab asset management is really important for many reasons. The API created would idnetify and address these. These include:
* planning and forecasting - lab equipment is really expensive (some instruments are 2million plus) and if older equipment are no longer supported by manufacturers, these instruments need to be replaced eventually. Planning for a replacement to meet the required workflow could take up to a year and due to the heavy investments, planning is essential. In the assests model, a date of purchased has been included so the age of the instrument is known. This would essentially help in future replacements
* Compliance - Generally most labs have to be compliant with regulatory requirements and standards in the clinical, pharma and diagnostic markets. This could include annual PM's (Preventaive Maintence) and qualifications to meet these standards. The API includes a service jobs model that includes a history of service jobs done on the instrument. A user would be able to track when the last PM or qualifiaction was done and be able to plan for te next one. 
* Risk Management - having a ideas of which instruments are most likely going to breakdown or have had a history of breaking down is important for a business. This will be able to be seen by the service job history of the instrument.
* 


## *Why have you chosen this database system. What are the drawbacks compared to others?*
The database system chosen for this project is PostgreSQL. Below are some of the reason why I have chosed PostgreSQL. 








## *Identify and discuss the key functionalities and benefits of an ORM*
A ORM (Object Realtional Mapping)




## *Document all endpoints for your API*

### View all employees
'GET' - ```@employees.route("/", methods=["GET"])```
* Example - http://127.0.0.1:5000/employees
* Authentication method - any USER
* Expected Response: 




### View all assets
'GET' - ```@assets.route("/", methods=["GET"])```
* Example - http://127.0.0.1:5000/assets
* Authentication method - any USER
* Expected Response: 


### View all manufacturers
'GET' - ```@manufacturers.route("/", methods=["GET"])```
* Example - http://127.0.0.1:5000/manufacturers
* Authentication method - any USER
* Expected Response: 

### View all departments
'GET' - ```@departments.route("/", methods=["GET"])```
* Example - http://127.0.0.1:5000/departments
* Authentication method - any USER
* Expected Response: 

### View all service jobs
'GET' - ```@service_job.route("/", methods=["GET"])```
* Example - http://127.0.0.1:5000/service_job
* Authentication method - any USER
* Expected Response: 

### View all assets in a department
'GET' - ```@departments.route('/assets/<int:department_id>', methods=["GET"])```
* Example - http://127.0.0.1:5000/departments/assets/1
* Authentication method - any USER
* Expected Response: 

### View assets a employee could have
'GET' - ```@employees.route('/assets/<int:employee_id>', methods=["GET"])```
* Example - http://127.0.0.1:5000/departments/assets/1
* Authentication method - any USER
* Expected Response: 

### View all manufacturers assets a department has
'GET' - 

RESPONSE:

### View all service history for the asset
'GET' - ```@assets.route('/service_job/<int:asset_id>', methods=["GET"])```
* Example - http://127.0.0.1:5000/departments/assets/1
* Authentication method - any USER
* Expected Response: 

### View details of one asset
'GET' - ```@assets.route("/<int:id>/", methods=["GET"])```
* Example - http://127.0.0.1:5000/assets/1
* Authentication method - any USER
* Expected Response: 

### View details of one employee
'GET' - ```@employees.route("/<int:id>/", methods=["GET"])```
* Example - http://127.0.0.1:5000/employees/1
* Authentication method - any USER
* Expected Response: 

### View details of one department
'GET' - ```@departments.route("/<int:id>/", methods=["GET"])```
* Example - http://127.0.0.1:5000/departments/1
* Authentication method - any USER
* Expected Response: 

### View details of one manufacterer 
'GET' - ```@manufacturers.route("/<int:id>/", methods=["GET"]))```
* Example - http://127.0.0.1:5000/manufacturers/1
* Authentication method - any USER
* Expected Response: 

### View details of one sevice job
'GET' - ```@service_job.route("/<int:id>/", methods=["GET"])```
* Example - http://127.0.0.1:5000/manufacturers/1
* Authentication method - any USER
* Expected Response: 

### Delete employee
'DELETE' - ```@employees.route("/<int:id>/", methods=["DELETE"])```
* Example - http://127.0.0.1:5000/employees/1
* Authentication method - ADMIN
* Expected Response: 


### Delete asset
'DELETE' - ```@assets.route("/<int:id>/", methods=["DELETE"])```
* Example - http://127.0.0.1:5000/assets/1
* Authentication method - ADMIN
* Expected Response: 

### Delete department
'DELETE' - ```@departments.route("/<int:id>/", methods=["DELETE"])```
* Example - http://127.0.0.1:5000/departments/1
* Authentication method - ADMIN
* Expected Response: 

### Delete manufacturer 
'DELETE' - ```@manufacturers.route("/<int:id>/", methods=["DELETE"])```
* Example - http://127.0.0.1:5000/manufacturers/3
* Authentication method - ADMIN
* Expected Response: 

### Delete service job 
'DELETE' - ```@@service_job.route("/<int:id>/", methods=["DELETE"])```
* Example - http://127.0.0.1:5000/service_job/7
* Authentication method - ADMIN
* Expected Response: 
  

### Add department
'POST' - ```@departments.route("/", methods=["POST"])```
* Example - http://127.0.0.1:5000/departments/
* Authentication method - ADMIN
* Expected Response

### Add employee
'POST' - ```@employees.route("/", methods=["POST"])```
* Example - http://127.0.0.1:5000/employees/
* Authentication method - ADMIN
* Expected Response: 

### Add asset
'POST' - ```@assets.route("/", methods=["POST"])```
* Example - http://127.0.0.1:5000/assets/
* Authentication method - ADMIN
* Expected Response

### Add manufacturer
'POST' - ```@manufacturers.route("/", methods=["POST"])```
* Example - http://127.0.0.1:5000/manufacturers/
* Authentication method - ADMIN
* Expected Response

### Add service job
'POST' - ```@service_job.route("/", methods=["POST"])```
* Example - http://127.0.0.1:5000/service_jobs/
* Authentication method - ADMIN
* Expected Response

### Add user




### Update department
'PUT' - ```@departments.route("/<int:id>/", methods=["PUT"])```
* Example - http://127.0.0.1:5000/departments/1
* Authentication method - ADMIN
* Expected Response



### Update employee
'PUT' - ```@employees.route("/<int:id>/", methods=["PUT"])```
* Example - http://127.0.0.1:5000/employees/1
* Authentication method - ADMIN
* Expected Response


### Update asset
'PUT' - ```@assets.route("/<int:id>/", methods=["PUT"])```
* Example - http://127.0.0.1:5000/assets/1
* Authentication method - ADMIN
* Expected Response

### Update manufacturer
'PUT' - ```@manufacturers.route("/<int:id>/", methods=["PUT"])```
* Example - http://127.0.0.1:5000/manufacturers/1
* Authentication method - ADMIN
* Expected Response


### Update service job
'PUT' - ```@service_job.route("/<int:id>/", methods=["PUT"])```
* Example - http://127.0.0.1:5000/service_job/1
* Authentication method - ADMIN
* Expected Response


## *An ERD for your app*
Please see the below for the ERD.


## *Detail any third party services that your app will use*

Bcrypt

Marshmallow

Werkzeug

## *Describe your projects models in terms of the relationships they have with each other*

### Department and Employees -
This is a one to many relationship. A employee can only belong to one department, while one department can have many employees. 

### Employees and Assets-
This is a one to many relationship. A employee can have many assets, while only one asset can only belong to employee

### Assets and Manufacturers
This is a one to many relationship. A asset only be manufactured by only one manufacturer while one manufacturer can manufacturer many different types of assets

### Assets and Service Histoy
This is a one to many relationship. A asset could only have the service job done for it, while there could be many service history jobs associated with that asset 

### Users
This is model only has access to the data in the tables and has no relationship in the ERD. Only with admin privliges can a user insert, update and delete data in the tables. A standard user can only view data in the tables

## *Discuss the database relations to be implemented in your application*
****





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

  

