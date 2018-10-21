from marshmallow import post_load

from .user import User, UserSchema
from .user_type import UserType


class Regular(User):
    """Represents the Store Attendant"""

    def __init__(self, user_name, password):
        super(Regular, self).__init__(user_name, password, UserType.REGULAR)

    def __repr__(self):
        return '<User(user_name={self.user_name!r, user_type={self.user_type}))>'.format(self=self)


class RegularSchema(UserSchema):
    @post_load()
    def make_attendant(self, data):
        return Regular(**data)
