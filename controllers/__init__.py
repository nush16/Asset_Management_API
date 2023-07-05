from controllers.auth_controller import auth
from controllers.department_controller import departments
from controllers.employee_controller import employees
from controllers.asset_controller import assets
from controllers.service_job_controller import service_job
from controllers.manufacturer_controller import manufacturers

registerable_controllers = [
    auth,
    departments,
    employees,
    assets,
    service_job,
    manufacturers,
]