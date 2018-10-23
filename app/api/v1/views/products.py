from flask import request, jsonify, make_response
from flask_classful import FlaskView, route

products = [
    {
        'id': 1,
        'p_name': 'Product 1',
        'p_price': 23.4,
        'p_quantity': 45
    },
    {
        'id': 2,
        'p_name': 'Product 2',
        'p_price': 45.6,
        'p_quantity': 56
    },
    {
        'id': 3,
        'p_name': 'Product 3',
        'p_price': 54.56,
        'p_quantity': 56
    }
]


class ProductView(FlaskView):
    """Product View Class"""

    def index(self):
        # TODO: return valid response if none exists
        return make_response(jsonify(products)), 200

    def post(self):
        post_data = request.data
        # if it exists
        if post_data:
            product = {
                'id': products[-1]['id'] + 1,
                "p_name": post_data['p_name'],
                "p_price": post_data['p_price'],
                "p_quantity ": post_data['p_quantity']
            }
            products.append(product)
            return make_response(jsonify(product)), 201

    @route('/<p_id>')
    def get(self, p_id):
        """Get item with id"""
        for i in range(len(products)):
            if products[i]['id'] == int(p_id):
                return make_response(jsonify(products[i])), 200
        else:
            response = {
                'status': 'Failed',
                'message': 'Product Not Found'
            }
            return make_response(jsonify(response)), 404
