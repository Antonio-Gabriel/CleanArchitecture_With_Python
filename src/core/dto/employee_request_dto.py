from dataclasses import dataclass, fields

from src.core.entities import Location


@dataclass(frozen=True)
class IEmployeeRequestDto:
    name: str
    email: str
    phone: int
    location: Location

    def __post_init__(self):
        """ Initialize the request object """

        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                raise ValueError(
                    f"Expected {field.name} to be {field.type} but got {repr(value)}"
                )

        self.__required_args()

    def __required_args(self):
        """ Return all required arguments"""

        for field in fields(self):
            value = getattr(self, field.name)
            if value == "" or None:
                raise TypeError(
                    f"Value {field.name} is required"
                )
