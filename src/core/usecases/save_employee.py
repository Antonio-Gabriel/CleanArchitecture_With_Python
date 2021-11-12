#!python3
from typing import Type
from src.core.entities import *

from src.core.repositories import IEmployeeRepository


class SaveEmployee:

    def __init__(self, employee_repository_interface: Type[IEmployeeRepository]):
        self.__employee_repository = employee_repository_interface()              


    def execute(self, **kwargs) -> Employee:       

        if self.__is_null_or_empty(**kwargs): 
            raise Exception("Error on Object, have a empty value")

        employee_data = Employee(
            name=kwargs["name"],
            email=kwargs["email"],
            phone=kwargs["phone"],
            location= Location(
                district=kwargs["district"],
                road=kwargs["road"],
                city=kwargs["city"]
                )
            )
                    
        if not employee_data.isValidPhoneNumber(**{
            "phone": kwargs["phone"]
        }): 
            raise Exception("The value of number is not valied!.")
                
        self.__employee_repository.save_employee(employee_data)  
        return employee_data.show_current_employee             
        
             
    def __is_null_or_empty(self, **kwargs) -> bool:
        for data in kwargs:
            if data == "" or None:
                return False
