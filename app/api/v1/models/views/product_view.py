from flask import request, jsonify
from flask_restful import Resource

from app.api.v1.models.views.regular_user_view import users
from .utils import requires_admin, requires_auth
from app.api.v1.models.item.product import Product, ProductSchema

products = [
    Product("Product 1", 23.0, 34, users[1]),
    Product("Product 2", 45.0, 19, users[1]),
    Product("Product 3", 45.5, 56, users[3]),
    Product("Product 4", 78.6, 45, users[3])
]


class ProductView(Resource):
    """represents endpoint for products"""

    @requires_auth
    def get(self, **id):
        schema = ProductSchema(many=True)
        all_products = schema.dump(products)
        if id is None:
            return {'status': 'success', 'data': all_products}, 200
        else:
            print(id['id'])
            pos = id['id']
            for i in range(len(all_products[0])):
                if id['id'] > len(all_products[0]) or pos < 1:
                    response = {
                        'message': 'Item doesnt Exist'
                    }
                    return response, 404
                else:
                    product = all_products[0][pos - 1]
                    return jsonify(product)

    @requires_admin
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input provided'}, 400
        data, errors = ProductSchema().load(json_data)
        if errors:
            return errors, 422
        product = Product(
            product_name=json_data['product_name'],
            product_price=json_data['product_price'],
            product_quantity=json_data['product_quantity'],
            added_by=users[1]  # TODO: get from login
        )
        for i in products:
            if i.item_name == product.item_name:
                return {'status': 'failed', 'message': 'product already exits'}, 201
        else:
            products.append(product)
            response = ProductSchema().dump(product).data
            return {'status': 'success', 'data': response}, 201
