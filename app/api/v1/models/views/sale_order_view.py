from flask import request
from flask_restful import Resource

from app.api.v1.models.views.regular_user_view import users
from .utils import requires_admin, requires_auth
from app.api.v1.models.item.sale_order import SaleOrder, SaleOrderSchema

sales = [
    SaleOrder("Sale 1", 23.0, 3, users[0]),
    SaleOrder("Sale 2", 45.0, 1, users[2]),
    SaleOrder("Sale 3", 45.5, 6, users[2]),
    SaleOrder("Sale 4", 78.6, 5, users[0])
]


class SaleOrderView(Resource):
    """represents endpoint for sales"""

    @requires_admin
    def get(self):
        schema = SaleOrderSchema(many=True)
        all_sales = schema.dump(sales)
        return {'status': 'success', 'data': all_sales}, 200
