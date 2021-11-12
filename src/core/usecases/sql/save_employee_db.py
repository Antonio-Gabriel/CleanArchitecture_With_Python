from typing import Type

from src.core.dto.employee_request_dto import IEmployeeRequestDto
from src.core.entities import Employee, Location
from src.core.repositories import IEmployeeRepository

class SaveEmployeeDb:

    def __init__(self, employee_repository_interface: Type[IEmployeeRepository]):
        self.__repository_interface = employee_repository_interface()
    

    def execute(self, employee_req_dto: Type[IEmployeeRequestDto]):
        """ Save the employee request"""

        employee_data = Employee(
            name=employee_req_dto.name,
            email=employee_req_dto.email,
            phone=employee_req_dto.phone,
            location= Location(
                district=employee_req_dto.location.district,
                road=employee_req_dto.location.road,
                city=employee_req_dto.location.city
                )
            )
                    
        if not employee_data.isValidPhoneNumber(**{
            "phone": employee_req_dto.phone
        }): 
            raise Exception("The value of number is not valied!.")   
        
        self.__repository_interface.save_employee(employee_data)

        return "OK"
