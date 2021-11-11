from collections import namedtuple
from typing import Type
from uuid import uuid4

from src.core.entities.location import Location

class Employee:

    def __init__(self, name: str, email: str, phone: int, location: Type[Location], id: str = None):   
        self.name  = name        
        self.email = email
        self.phone = phone
        self.id = id     

        # association with location object
        self.location = location

        self.__generate_id(id)
        

    @property
    def isValidPhoneNumber(self):
        """Returns true if phone number is valid"""

        if len(self.phone) < 9: 
            return False             
    

    def __generate_id(self, id):
        if id is None:
            self.id = uuid4()

    def show_current_employee(self) -> namedtuple:
        employee_struc = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "location": {
                "district": self.location.district,
                "city": self.location.city,
                "road": self.location.road
            }
        }

        return namedtuple("Employee", **employee_struc)        