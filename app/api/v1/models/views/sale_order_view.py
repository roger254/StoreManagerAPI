from flask import request
from flask_restful import Resource

from app.api.v1.models.views.regular_user_view import users
from .utils import requires_admin, requires_auth
from app.api.v1.models.item.sale_order import SaleOrder, SaleOrderSchema

sales = [
    SaleOrder("Sale 1", 34.5, 3, users[0]),
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

    @requires_admin
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input provided'}, 400
        data, errors = SaleOrderSchema().load(json_data)
        if errors:
            return errors, 422
        sale = SaleOrder(
            sale_name=json_data['sale_name'],
            sale_price=json_data['sale_price'],
            sale_quantity=json_data['sale_quantity'],
            created_by=users[1]  # TODO: get from login
        )
        for i in sales:
            if i.item_name == sale.item_name:
                return {'status': 'failed', 'message': 'product already exits'}, 201
        else:
            sales.append(sale)
            response = SaleOrderSchema().dump(sales).data
            return {'status': 'success', 'data': response}, 201
