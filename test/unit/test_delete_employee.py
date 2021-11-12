from unittest import TestCase
from src.core.dto.employee_dto import EmployeeDTO

from src.core.usecases import DeleteEmployee
from src.infra.repository import EmployeeRepositoryMemory

class TestDeleteEmployee(TestCase):

    def test_delete_employee(self):

        employee = DeleteEmployee(EmployeeRepositoryMemory)
        employee.execute(EmployeeDTO(id=1))

        self.assertTrue(True)