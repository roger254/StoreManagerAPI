from flask import jsonify, request, make_response
from flask_restful import Resource
from .utils import requires_admin, requires_attendant
from app.api.v1.models.regular import Regular, RegularSchema
from app.api.v1.models.admin import Admin, AdminSchema
from app.api.v1.models.user_type import UserType

users = [
    Regular('Attendant 1', 'pass_att1'),
    Admin('Owner 1', 'owner_pass'),
    Regular('Attendant 2', 'pass_att'),
    Admin('Owner 2', 'owner2_pass')
]


class AddRegularUser(Resource):
    """represents endpoint for regular user"""

    @requires_admin
    def get(self):
        schema = RegularSchema(many=True)
        admins = schema.dump(
            filter(lambda t: t.user_type == UserType.REGULAR, users)
        )
        return jsonify(admins.data)

    @requires_admin
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input provided'}, 400
        data, errors = RegularSchema().load(json_data)
        if errors:
            return errors, 422
        attendant = Regular(
            user_name=json_data['user_name'],
            password=json_data['password']
        )
        for i in users:
            if i.user_name == attendant.user_name:
                return {'status': 'failed', 'message': 'user already exits'}, 201
        else:
            users.append(attendant)
            response = RegularSchema().dump(attendant).data
            return {'status': 'success', 'data': response}, 201
