#!python3

from dataclasses import dataclass, fields
from typing import Type

@dataclass(frozen=False, init=True)
class IPersonRequestDTO:
    name: str
    email: int

    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                raise ValueError(
                    f"Expected {field.name} to be {field.type}, got {repr(value)}"
                    )
        self.__required_args()

    def __required_args(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if value == "" or None:
                raise TypeError(
                    f"Value {field.name} is required"
                    )

def save(person_request: Type[IPersonRequestDTO]):   
    print(person_request)
    
save(IPersonRequestDTO(name="Ag", email=""))