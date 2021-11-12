#!python3

from dataclasses import dataclass, fields
from typing import Type

@dataclass(frozen=True)
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

def save(person_request: Type[IPersonRequestDTO]):
    print(person_request)

save(IPersonRequestDTO(name="ag", email=0))
