from functools import wraps
from flask import request, make_response, jsonify
from app.api.v1 import views
from .models.admin import Admin, AdminSchema
from .models.admin import UserType


def requires_auth(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        auth = request.authorization
        if auth:
            schema = AdminSchema(many=True)
            admins = schema.dump(
                filter(lambda t: t.user_type == UserType.ADMIN, views.users)
            )

            for i in admins.data:
                if i['user_name'] == auth.username and i['password'] == auth.password:
                    return f(*args, **kwargs)

        return make_response("Authentication Required", 401, {'WWW-Authenticate': 'Basic realm="Login Required'})

    return wrapped
