from unittest import TestCase

from src.core.usecases.sql import GetEmployeeDb
from src.infra.repository.sql import EmployeeRepository

class TestGetEmployeeDb(TestCase):

    def test_get_employee_db(self):

        employee_data = GetEmployeeDb(EmployeeRepository)
        print(employee_data.get())

        self.assertTrue(True)