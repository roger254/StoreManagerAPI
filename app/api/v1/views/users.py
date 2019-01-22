from flask import request, jsonify, make_response
from flask_classful import FlaskView, route

from .auth import generate_user_token

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

    @route('/register', methods=['POST'])
    def post(self):
        """Get user data"""
        post_data = request.data
        # if it exists
        user = request.data['user_name']
        for i in range(len(users)):
            if users[i]['user_name'] == user:
                message = {
                    'status': 'Registration Failed',
                    'message': 'User Exists. Please Log in!'
                }
                return make_response(jsonify(message)), 202
        else:
            if post_data:
                user = {
                    'id': users[-1]['id'] + 1,
                    "user_name": post_data['user_name'],
                    "password": post_data['password'],
                    "user_type": 'Attendant'
                }
                users.append(user)
                return make_response(jsonify(user)), 201

    @route('/login', methods=['POST'])
    def login(self):
        try:
            user = request.data['user_name']
            user_pass = request.data['password']
            for i in range(len(users)):
                if users[i]['user_name'] == user and users[i]['password'] == user_pass:
                    access_token = generate_user_token(users[i]['id'])
                    if access_token:
                        response = {
                            "message": "You've logged in successfully.",
                            "access_token": access_token.decode()
                        }

                        return make_response(jsonify(response)), 200
            else:
                response = {
                    "message": "Invalid username or password, Please try again"
                }
                return make_response(jsonify(response)), 401
        except Exception as e:
            response = {
                'message': str(e)
            }
            return make_response(jsonify(response)), 500
