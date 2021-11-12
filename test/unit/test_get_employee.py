from unittest import TestCase

from src.core.usecases import SaveEmployee, GetEmployee
from src.infra.repository import EmployeeRepositoryMemory

class TestGetEmployee(TestCase):

    def test_employee_entitty(self):
        employee_data = SaveEmployee(EmployeeRepositoryMemory)
        employee_data.execute(
            **{
                "name": "ag",
                "email": "ag@example.com",
                "phone": 998987890,
                "district": "New York",
                "city": "New York",
                "road": "New York"
            }
        )

        employee = GetEmployee(EmployeeRepositoryMemory)
        print(employee.execute())

        self.assertTrue(True)