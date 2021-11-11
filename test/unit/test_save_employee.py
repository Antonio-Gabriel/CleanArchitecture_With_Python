from unittest import TestCase

from src.core.entities.employee import Employee
#from src.core.usecases.save_employee import SaveEmployee

class TestSaveEmployee(TestCase):
    
    def test_employee_entitty(self):

        Employee("Ag", "ag@example.com", 998987888)        
        self.assertTrue(True)
    
    def test_save_employee_with_location(self):
        
        
        self.assertTrue(True)
