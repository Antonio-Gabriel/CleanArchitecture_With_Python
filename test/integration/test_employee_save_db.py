from unittest import TestCase

from src.core.dto import IEmployeeRequestDto
from src.infra.repository.sql import EmployeeRepository
from src.core.usecases.sql import SaveEmployeeDb

from src.core.entities import Location

class EmployeeSaveDb(TestCase):

    def test_save_employee_db(self):

        employee_data = SaveEmployeeDb(EmployeeRepository)
        response = employee_data.execute(
            IEmployeeRequestDto(
                    name='António Campos Gabriel', 
                    email='test@example.com', 
                    phone=998987689,
                    location= Location(
                        district="Hoji-ya-henda",
                        city='Luanda',
                        road="Zamba4"
                    )
                )
            )

        print(response.name)
        
        self.assertTrue(True)