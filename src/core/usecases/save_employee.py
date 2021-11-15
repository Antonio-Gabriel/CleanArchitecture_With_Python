from typing import Type
from src.adapter import EmployeeAdapter
from src.core.entities import *

from src.core.repositories import IEmployeeRepository


class SaveEmployee:

    def __init__(self, employee_repository_interface: Type[IEmployeeRepository]):
        self.__employee_repository = employee_repository_interface()        


    def execute(self, **kwargs) -> Employee:       
        """ Save the employee and return the employee
            :param kwargs: keyword arguments of employee
        """

        if not self.__is_null_or_empty(**kwargs): 
            raise Exception("Error on Object, have a empty value")

        employee_data = EmployeeAdapter.create(
            kwargs["name"], kwargs["email"], 
            kwargs["phone"], kwargs["district"], 
            kwargs["road"], kwargs["city"]
            )
                    
        if not employee_data.isValidPhoneNumber(**{
            "phone": kwargs["phone"]
        }): 
            raise Exception("The value of number is not valied!.")
                
        self.__employee_repository.save_employee(employee_data)  
        return employee_data.show_current_employee             
        
             
    def __is_null_or_empty(self, **kwargs) -> bool:
        """ Check if the employee is null or empty
            :param kwargs: keyword arguments of employee
        """

        for data in kwargs.values():
            if data is "" or None:
                return False
        return True
