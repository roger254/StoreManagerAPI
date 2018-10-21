from marshmallow import post_load

from app.api.v1.models.item.item import Item, ItemShema
from .item_type import ItemType


class Product(Item):
    """Represents the Store Products"""

    def __init__(self, product_name, product_price, product_quantity):
        super(Product, self).__init__(product_name, product_price, product_quantity, ItemType.PRODUCT)

    def __repr__(self):
        return '<Product(product_name={self.product_name!r}, ' \
               'product_price={self.product_price}, ' \
               'product_quantity={self.product_quantity))>'.format(self=self)


class ProductSchema(ItemShema):
    @post_load()
    def make_product(self, data):
        return Product(**data)
