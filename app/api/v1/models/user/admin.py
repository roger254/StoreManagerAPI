from marshmallow import post_load

from app.api.v1.models.user.user import UserSchema, User
from .user_type import UserType


class Admin(User):
    """Represents the Admin or Owner"""

    def __init__(self, user_name, password):
        super(Admin, self).__init__(user_name, password, UserType.ADMIN)

    def __repr__(self):
        return '<User(user_name={self.user_name!r}, user_type={self.user_type}))>'.format(self=self)


class AdminSchema(UserSchema):
    @post_load()
    def make_admin(self, data):
        return Admin(**data)
