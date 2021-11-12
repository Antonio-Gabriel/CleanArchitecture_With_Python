from typing import List, Type
from src.core.entities import Employee
from src.core.repositories import IEmployeeRepository

class EmployeeRepositoryMemory(IEmployeeRepository):
    
    def __init__(self):
        self.__storage = []
    

    def save_employee(self, employee: Type[Employee]) -> None:
        """ save the employee"""
        
        self.__storage.append(employee)


    def get_employees(self) -> List[Employee]:
        """ Get all employee"""
        return self.__storage
    

    def delete_employee(self, id: str) -> Employee:
        """ Delete the given employee"""

        raise Exception("Method not implemented.")
    