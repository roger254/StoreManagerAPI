import datetime as date
from marshmallow import Schema, fields


class User:
    """Represents The User Model"""

    def __init__(self, user_name, password, user_type):
        self.user_name = user_name
        self.password = password
        self.user_type = user_type
        self.date_created = date.datetime.now()

    def __repr__(self):
        return '<User(user_name={self.user_name!r} user_type={self.user_type})>'.format(self=self)


# to serialize and deserialize user from and to json obj
class UserSchema(Schema):
    """ Represents Fields for user"""
    user_name = fields.Str()
    password = fields.Str()
    user_type = fields.Str()
    date_created = fields.Date()
