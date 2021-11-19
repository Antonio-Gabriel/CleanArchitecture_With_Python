from typing import Type

from src.core.repositories import IEmployeeRepository


class GetEmployeeDb:

    def __init__(self, employee_repository_interface: Type[IEmployeeRepository]):
        self.__repository_interface = employee_repository_interface()

    def get(self):
        """ Returns the employee with location"""

        return self.__repository_interface.get_employees()
