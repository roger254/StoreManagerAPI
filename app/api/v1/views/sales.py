from flask import request, jsonify, make_response
from flask_classful import FlaskView, route

from .auth import authenticate
from ..models.items.sale import Sale

sales = [
    Sale(1, 'Sale 1', 34.6, 5, 'User 1'),
    Sale(2, 'Sale 2', 65.7, 2, 'User 2'),
    Sale(3, 'Sale 3', 56.7, 2, 'User 3'),
    Sale(4, 'Sale 4', 45.6, 1, 'User 3'),
    Sale(5, 'Sale 5', 56.7, 5, 'User 4'),
]


class SaleView(FlaskView):
    """Product View Class"""
    decorators = [authenticate]

    def index(self):
        # TODO: return valid response if none exists
        response = {
            'status': 'Items Found',
            'sales': list(map(f, sales))
        }
        return response, 201

    def post(self, ):

        post_data = request.data
        # if it exists
        s_name = request.data['s_name']
        s_price = request.data['s_price']
        s_quantity = request.data['s_quantity']
        sale = Sale(
            len(sales) + 1,
            s_name,
            float(s_price),
            int(s_quantity),
            'User 3'
        )
        invalid_product = sale.validate_data()
        if invalid_product:
            return make_response(jsonify(invalid_product)), 208
        for i in range(len(sales)):
            if sales[i].item_name == sale.item_name:
                message = {
                    'status': 'Adding Failed',
                    'message': 'Item Already Exists'
                }
                return make_response(jsonify(message)), 202
        else:
            if post_data:
                sales.append(sale)
                # TODO: return product details
                return make_response(jsonify(sale.details())), 201

    @route('/<p_id>')
    def get(self, p_id):
        """Get item with id"""
        for i in range(len(sales)):
            if sales[i].item_id == int(p_id):
                sale = sales[i]
                return make_response(jsonify(sale.details())), 200
        else:
            response = {
                'status': 'Failed',
                'message': 'Sale Item Not Found'
            }
            return make_response(jsonify(response)), 404


def f(n):
    return n.details()
