from main import db

class ServiceJob(db.Model):
    # define the table name for the db as assets
    __tablename__= "service_jobs"
    # Set the primary key
    service_job_id = db.Column(db.Integer,primary_key=True)
    # the rest of the attributes/columns
    service_description  = db.Column(db.String(), nullable=False) 
    service_date = db.Column(db.Date(), nullable=False)
    # link to assets
    asset_id = db.Column(db.Integer, db.ForeignKey("assets.asset_id"), nullable =False)
    