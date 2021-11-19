from typing import Type

from src.core.dto.employee_dto import EmployeeDTO
from src.core.repositories import IEmployeeRepository


class DeleteEmployee:

    def __init__(self, employee_repository_interface: Type[IEmployeeRepository]):
        self.__employee_repository = employee_repository_interface()

    def execute(self, employee_request: Type[EmployeeDTO]):
        """ Delete the employee
            :param id: The id of the employee
        """

        self.__employee_repository.delete_employee(employee_request.id)
