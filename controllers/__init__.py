from controllers.auth_controller import auth
from controllers.department_controller import departments
from controllers.employee_controller import employees
from controllers.asset_controller import assets
from controllers.asset_type_controller import asset_type
from controllers.manufacturer_controller import manufacturers

registerable_controllers = [
    auth,
    departments,
    employees,
    assets,
    asset_type,
    manufacturers,
]