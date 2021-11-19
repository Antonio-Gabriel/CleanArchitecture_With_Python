from collections import namedtuple
from typing import Type
from uuid import uuid4

from src.core.entities.location import Location


class Employee():

    def __init__(self, name: str, email: str, phone: int, location: Type[Location], id: str = None):

        self.id = self.__generate_id(id)
        self.name = name
        self.email = email
        self.phone = phone

        # association with location object
        self.location = location

    def isValidPhoneNumber(self, **kwargs) -> bool:
        """Returns true if phone number is valid"""

        if len(str(kwargs["phone"])) != 9:
            return False

        return True

    def __generate_id(self, id):
        """ __generate_id """

        if id is None:
            return uuid4()
        return id

    @property
    def show_current_employee(self):
        """ Returns """

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

        employee = namedtuple("Employee", employee_struc)
        return employee(**employee_struc)
