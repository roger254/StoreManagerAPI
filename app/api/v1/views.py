from flask import jsonify, request, make_response
from flask_restful import Resource
from .utils import requires_auth
from app.api.v1.models.regular import Regular, RegularSchema
from app.api.v1.models.admin import Admin, AdminSchema
from app.api.v1.models.user_type import UserType

users = [
    Regular('Attendant 1', 'pass_att1'),
    Admin('Owner 1', 'owner_pass'),
    Regular('Attendant 2', 'pass_att'),
    Admin('Owner 2', 'owner2_pass')
]


class Add_Regular_User(Resource):

    @requires_auth
    def get(self):
        schema = RegularSchema(many=True)
        admins = schema.dump(
            filter(lambda t: t.user_type == UserType.REGULAR, users)
        )
        return jsonify(admins.data)

    @requires_auth
    def post(self):
        regular = RegularSchema().load(request.get_json())
        users.append(regular.data)

        return '', 204
