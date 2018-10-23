from functools import wraps
from flask import request, make_response
from app.api.v1.models.views import regular_user_view
from app.api.v1.models.user.admin import AdminSchema
from app.api.v1.models.user.user import UserSchema
from app.api.v1.models.user.regular import RegularSchema
from app.api.v1.models.user.admin import UserType


# TODO : use token based
def requires_attendant(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        auth = request.authorization
        if auth:
            schema = RegularSchema(many=True)
            admins = schema.dump(
                filter(lambda t: t.user_type == UserType.REGULAR, regular_user_view.users)
            )
            for i in admins.data:
                if i['user_name'] == auth.username and i['password'] == auth.password:
                    return f(*args, **kwargs)

        return make_response("Authentication Required", 401,
                             {'WWW-Authenticate': 'Basic realm="Login Required As Attendant'})

    return wrapped


def requires_admin(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        auth = request.authorization
        if auth:
            schema = AdminSchema(many=True)
            admins = schema.dump(
                filter(lambda t: t.user_type == UserType.ADMIN, regular_user_view.users)
            )
            for i in admins.data:
                if i['user_name'] == auth.username and i['password'] == auth.password:
                    return f(*args, **kwargs)

        return make_response("Authentication Required", 401,
                             {'WWW-Authenticate': 'Basic realm="Login Required as Admin'})

    return wrapped


def requires_auth(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        auth = request.authorization
        if auth:
            schema = UserSchema(many=True)
            users = schema.dump(regular_user_view.users)
            for i in users.data:
                if i['user_name'] == auth.username and i['password'] == auth.password:
                    return f(*args, **kwargs)
        return make_response("Authentication Required", 401,
                             {'WWW-Authenticate': 'Basic realm="Login Required'})

    return wrapped
