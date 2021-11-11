from abc import ABC, abstractmethod
from typing import List

from core.entities import Employee


class IEmployeeRepository(ABC):
    """ Represents a repository for employee"""
    
    @abstractmethod
    def save_employee() -> None:
        """ save the employee"""

        raise NotImplementedError("Method not implemented.")

    @abstractmethod
    def get_employee() -> List[Employee]:
        """ Get all employee"""

        raise NotImplementedError("Method not implemented.")
    
    @abstractmethod
    def delete_employee(id: str) -> Employee:
        """ Delete the given employee"""

        raise NotImplementedError("Method not implemented.")