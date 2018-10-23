from flask import request, jsonify, make_response
from flask_classful import FlaskView

users = [
    {
        'id': 1,
        'user_name': 'User 1',
        'password': "test123",
        'user_type': 'Attendant'
    },
    {
        'id': 2,
        'user_name': 'User 2',
        'password': "test234",
        'user_type': 'Attendant'
    },
    {
        'id': 1,
        'user_name': 'Admin 1',
        'password': "admin123",
        'user_type': 'Admin'
    }
]


class UserView(FlaskView):
    """Product View Class"""

    def post(self):
        """Ger user data"""
        post_data = request.data
        # if it exists
        if post_data:
            user = {
                'id': users[-1]['id'] + 1,
                "user_name": post_data['user_name'],
                "password": post_data['password'],
                "user_type": 'Attendant'
            }
            users.append(user)
            return make_response(jsonify(user)), 201
