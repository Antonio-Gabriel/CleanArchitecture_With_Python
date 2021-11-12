from typing import Type

from src.core.repositories import IEmployeeRepository


class GetEmployee:
    
    def __init__(self, employee_repository_interface: Type[IEmployeeRepository]):
        self.__employee_repository = employee_repository_interface()

    def execute(self):
        """ Get all employee"""
        
        return self.__employee_repository.get_employees()