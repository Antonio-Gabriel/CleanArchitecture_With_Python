from dataclasses import dataclass, fields
from typing import Type

@dataclass(frozen=True)
class EmployeeDTO:
    id: int

    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                raise ValueError(
                    f"Expected {field.name} to be of type {field.type}, got {repr(value)}"
                    )