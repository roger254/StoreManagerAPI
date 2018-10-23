from flask_classful import FlaskView
from flask import request, jsonify, make_response

products = []


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
