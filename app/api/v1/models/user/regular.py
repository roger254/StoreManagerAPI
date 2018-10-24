from app.api.v1.models.user.user import User
from .user_type import UserType


class Regular(User):
    """Represents the Store Attendant"""

    def __init__(self, user_id, user_name, password):
        super(Regular, self).__init__(user_id, user_name, password, UserType.REGULAR)