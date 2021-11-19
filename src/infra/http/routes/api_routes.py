from flask import Blueprint, jsonify

api_routes_bp = Blueprint('api_routes', __name__)

@api_routes_bp.route('/', methods=['GET'])
def hello():
    return jsonify({"msg": "hello world"})