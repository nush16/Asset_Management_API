from main import ma

class ServiceJobSchema(ma.Schema):
    class Meta:
        ordered = True
        # fields to expose
        fields = ("service_job_id", "service_description", "service_date", "asset_id")

# single asset schema
service_job_schema = ServiceJobSchema()
# multiple asset schema
service_jobs_schema = ServiceJobSchema(many=True)