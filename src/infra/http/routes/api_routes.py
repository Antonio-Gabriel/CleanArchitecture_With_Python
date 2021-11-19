from flask import Blueprint, jsonify, request
from src.controller.employee_controller import EmployeeController

api_routes_bp = Blueprint('api_routes', __name__)

@api_routes_bp.route('/', methods=['GET'])
def hello():
    """ first route """

    employee_controller = EmployeeController()
    response = employee_controller.route(request)

    return jsonify({"msg": "hello world", "data": response.body})