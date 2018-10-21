from flask import Blueprint, request, make_response

from flask_restful import Api
from app.api.v1.views import Add_Regular_User

api_blue = Blueprint('api', __name__)
api = Api(api_blue)

# add route


api.add_resource(Add_Regular_User, '/users')
