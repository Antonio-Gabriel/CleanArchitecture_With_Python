from typing import Type

from src.infra.helpers import HttpRequest, HttpResponse
from src.main import IRouter

from src.core.usecases.sql import GetEmployeeDb
from src.infra.repository.sql import EmployeeRepository

class GetEmployeeController(IRouter):
    
    def __init__(self):
        self.__get_employee = GetEmployeeDb(EmployeeRepository)

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        
        storage = []
        for employee in self.__get_employee.get():
            storage.append({
                "name": employee[0],
                "email": employee[1],
                "phone": employee[2],
                "location": {
                    "district": employee[3],
                    "city": employee[4],
                    "road": employee[5]
                }
            })

        return HttpResponse(status_code=200, body=storage)        