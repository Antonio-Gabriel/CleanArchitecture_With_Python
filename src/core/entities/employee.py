from typing import Type
from uuid import uuid4

from core.entities.location import Location

class Employee:

    def __init__(self, name: str, email: str, phone: int, id: str = None):   
        self.name  = name        
        self.email = email
        self.phone = phone
        self.id = id     

        self.location = Type[Location]

        if id is None:
            self.id = uuid4()


    def isValid(self):
        pass