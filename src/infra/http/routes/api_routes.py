from flask import Blueprint, jsonify, request
from src.controller import EmployeeController
from src.adapter import FlaskAdapter

api_routes_bp = Blueprint('api_routes', __name__)


@api_routes_bp.route('/', methods=['POST'])
def create():
    """ first route """

    adapter = FlaskAdapter()
    response = adapter.execute(request, EmployeeController())

    return jsonify({"status_code": response.status_code, "data": [response.body]})


@api_routes_bp.route('/employee', methods=['GET'])
def get_employee_with_location():
    """ return employee """

    adapter = FlaskAdapter()
    response = adapter.execute(request, EmployeeController())

    return jsonify({"status_code": response.status_code, "data": [response.body]})
