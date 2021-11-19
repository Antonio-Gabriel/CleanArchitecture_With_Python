from flask import Blueprint, jsonify, request
from src.controller import EmployeeController
from src.adapter import FlaskAdapter

api_routes_bp = Blueprint('api_routes', __name__)


@api_routes_bp.route('/', methods=['GET'])
def hello():
    """ first route """

    # employee_controller = EmployeeController()
    # response = employee_controller.route(request)

    adapter = FlaskAdapter()
    response = adapter.execute(request, EmployeeController())

    return jsonify({"status_code": response.status_code, "data": response.body})
