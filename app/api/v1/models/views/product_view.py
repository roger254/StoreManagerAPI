from flask import request
from flask_restful import Resource
from .utils import requires_admin
from app.api.v1.models.item.product import Product, ProductSchema

products = [
    Product("Product 1", 23.0, 34),
    Product("Product 2", 45.0, 19),
    Product("Product 3", 45.5, 56),
    Product("Product 4", 78.6, 45)
]


class ProductView(Resource):
    """represents endpoint for products"""

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
            product_quantity=json_data['product_quantity']
        )
        for i in products:
            if i.item_name == product.item_name:
                return {'status': 'failed', 'message': 'product already exits'}, 201
        else:
            products.append(product)
            response = ProductSchema().dump(product).data
            return {'status': 'success', 'data': response}, 201
