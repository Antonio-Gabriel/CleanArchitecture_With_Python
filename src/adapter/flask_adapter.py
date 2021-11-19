from typing import Type
from src.infra.helpers import HttpRequest
from src.infra.helpers.http_models import HttpResponse

from src.main import IRouter
from src.infra.errors import HttpErrors


class FlaskAdapter:

    def execute(self, http_request: any, api_controller: Type[IRouter]) -> any:
        """ Adapter of Flask 
            :param - Flask Request
            :param - api controller
        """

        try:

            query_string_params = http_request.args.to_dict()

        except:
            http_error = HttpErrors._400()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        https_request = HttpRequest(
            headers=http_request.headers, body=http_request.json, query=query_string_params
        )

        try:

            response = api_controller.route(https_request)            

        except:
            http_error = HttpErrors._500()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return response
