from flask import request, jsonify, make_response
from flask_classful import FlaskView, route

sales = [
    {
        'id': 1,
        's_name': 'Sale 1',
        's_price': 23.4,
        's_quantity': 45,
        'sold_by': 'User1'
    },
    {
        'id': 2,
        's_name': 'Sale 2',
        's_price': 45.6,
        's_quantity': 56,
        'sold_by': 'User 1'
    },
    {
        'id': 3,
        's_name': 'Sale 3',
        's_price': 54.56,
        's_quantity': 56,
        'sold_by': 'User 2'
    }
]


class SaleView(FlaskView):
    """Product View Class"""

    def index(self):
        """returns all sale records"""
        # TODO: return best response when empty
        return make_response(jsonify(sales)), 200

    def post(self):
        post_data = request.data
        # if it exists
        if post_data:
            sale = {
                'id': sales[-1]['id'] + 1,
                "s_name": post_data['s_name'],
                "s_price": post_data['s_price'],
                "s_quantity ": post_data['s_quantity'],
                'sold_by': 'User 1'
            }
            sales.append(sale)
            return make_response(jsonify(sale)), 201

    @route('/<s_id>')
    def get(self, s_id):
        for i in range(len(sales)):
            if sales[i]['id'] == int(s_id):
                return make_response(jsonify(sales[i])), 200
        else:
            response = {
                'status': 'Failed',
                'message': 'Sale Not Found'
            }
            return make_response(jsonify(response)), 404
