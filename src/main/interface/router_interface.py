from typing import Type
from abc import ABC, abstractmethod
from src.infra.helpers import HttpRequest, HttpResponse

class IRouter(ABC):
    """ Router Interface """    

    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Router rule """

        raise NotImplementedError("Method not implemented")