from typing import Type
from src.infra.helpers import HttpRequest, HttpResponse
from src.main import IRouter

class EmployeeController(IRouter):

    def __init__(self):
        pass

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Employee route for get """
        
        return HttpResponse(status_code=200, body={"name": http_request.body["name"]})