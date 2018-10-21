from flask import Blueprint

from flask_restful import Api
from app.api.v1.models.views.regular_user_view import RegularUserView

api_blue = Blueprint('api', __name__)
api = Api(api_blue)

# add route
api.add_resource(RegularUserView, '/users')

from app.api.v1.models.views.product_view import ProductView

api.add_resource(ProductView, '/products')
