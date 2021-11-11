from typing import Type
from core.entities.employee import Employee

from core.repositories import IEmployeeRepository
from src.core.entities.location import Location

class SaveEmployee:

    def __init__(self):
        self.employee_repository = IEmployeeRepository()

    def execute(self, **kwargs):

        employee_data = Employee(
            name=kwargs["name"],
            email=kwargs["email"],
            phone=kwargs["phone"],
            location= Location(
                    district=kwargs["district"],
                    city=kwargs["city"],
                    road=kwargs["road"]
                )
            )

        if employee_data.isValidPhoneNumber: 
            raise Exception("The value of number id not valied!.")
        
        self.employee_repository.save_employee(employee_data)        