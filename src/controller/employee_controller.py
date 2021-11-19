from typing import Type
from src.core.entities import Location
from src.infra.errors.http_errors import HttpErrors
from src.infra.helpers import HttpRequest, HttpResponse
from src.main import IRouter

from src.core.usecases.sql import SaveEmployeeDb
from src.infra.repository.sql import EmployeeRepository
from src.core.dto import IEmployeeRequestDto


class EmployeeController(IRouter):

    def __init__(self):
        self.__save_employee_use_case = SaveEmployeeDb(EmployeeRepository)

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Employee route for get """

        if http_request.body or http_request.query:

            response = self.__save_employee_use_case.execute(IEmployeeRequestDto(
                name=http_request.body["name"],
                email=http_request.body["email"],
                phone=int(http_request.body["phone"]),
                location=Location(
                    city=http_request.body["city"],
                    district=http_request.body["district"],
                    road=http_request.body["road"]
                )
            ))

            response_body = {
                "name": response.name,
                "email": response.email,
                "phone": response.phone,
                "location": {
                    "district": response.location["district"],
                    "city": response.location["city"],
                    "road": response.location["road"],
                },
            }

            return HttpResponse(status_code=200, body=response_body)

        http_error = HttpErrors._400()
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
