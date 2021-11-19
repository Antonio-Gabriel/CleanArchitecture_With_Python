from typing import Type

from src.core.entities import Employee, Location
from src.core.dto.employee_request_dto import IEmployeeRequestDto
from src.core.repositories import IEmployeeRepository
from src.adapter import EmployeeAdapter


class SaveEmployeeDb:

    def __init__(self, employee_repository_interface: Type[IEmployeeRepository]):
        self.__repository_interface = employee_repository_interface()

    def execute(self, employee_req_dto: Type[IEmployeeRequestDto]):
        """ Save the employee request"""

        employee_data = EmployeeAdapter.create(
            employee_req_dto.name, employee_req_dto.email,
            employee_req_dto.phone, employee_req_dto.location.district,
            employee_req_dto.location.road, employee_req_dto.location.city
        )

        if not employee_data.isValidPhoneNumber(**{
            "phone": employee_req_dto.phone
        }):
            raise Exception("The value of number is not valied!.")

        self.__repository_interface.save_employee(employee_data)

        return employee_data.show_current_employee
