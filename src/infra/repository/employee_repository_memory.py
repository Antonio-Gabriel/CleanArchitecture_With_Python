from typing import List, Type
from src.core.entities import Employee
from src.core.repositories import IEmployeeRepository

class EmployeeRepositoryMemory(IEmployeeRepository):
    
    def __init__(self):
        self.__storage = [
            {
                "name": "ag",
                "email": "ag@example.com",
                "phone": 998987890,
                "district": "New York",
                "city": "New York",
                "road": "New York"
            }
        ]
    

    def save_employee(self, employee: Type[Employee]) -> None:
        """ save the employee"""
        
        self.__storage.append(employee)


    def get_employees(self) -> List[Employee]:
        """ Get all employee"""
        return self.__storage
    

    def delete_employee(self, id: int) -> Employee:
        """ Delete the given employee"""

        print(id)
    