from unittest import TestCase

from src.core.entities.employee import Employee
from src.core.entities.location import Location

from src.core.usecases import SaveEmployee
from src.infra.repository import EmployeeRepositoryMemory



class TestSaveEmployee(TestCase):
    
    def test_employee_entitty(self):

        Employee("Ag", "ag@example.com", 998987888, 
        Location("Newyork","Newyork", "US"))      
        
        self.assertTrue(True)
    
    def test_save_employee_with_location(self):

        employee_data = SaveEmployee(EmployeeRepositoryMemory)
        employee = employee_data.execute(
            **{
                "name": "Ag",
                "email": "ag@example.com",
                "phone": 998987890,
                "district": "New York",
                "city": "New York",
                "road": "New York"
            }
        )
        
        print(employee)
        self.assertTrue(True)
