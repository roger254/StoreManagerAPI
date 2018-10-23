from flask import request, jsonify, make_response
from flask_classful import FlaskView

products = [
    {
        'p_name': 'Product 1',
        'p_price': 23.4,
        'p_quantity': 45
    },
    {
        'p_name': 'Product 2',
        'p_price': 45.6,
        'p_quantity': 56
    },
    {
        'p_name': 'Product 3',
        'p_price': 54.56,
        'p_quantity': 56
    }
]


class ProductView(FlaskView):
    """Product View Class"""

    def post(self):
        post_data = request.data
        # if it exists
        if post_data:
            product = {
                "p_name": post_data['p_name'],
                "p_price": post_data['p_price'],
                "p_quantity ": post_data['p_quantity']
            }
            products.append(product)
            return make_response(jsonify(product)), 201

    def get(self):
        # TODO: return valid response if none exists
        return make_response(jsonify(products)), 200
