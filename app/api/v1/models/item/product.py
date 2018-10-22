from marshmallow import post_load

from app.api.v1.models.item.item import Item, ItemSchema
from .item_type import ItemType


class Product(Item):
    """Represents the Store Products"""

    def __init__(self, product_name, product_price, product_quantity, added_by):
        self.item_type = ItemType.PRODUCT
        super(Product, self).__init__(product_name, product_price, product_quantity, added_by)

    def __repr__(self):
        return '<Product(product_name={self.item_name!r}, ' \
               'product_price={self.item_price}, ' \
               'product_quantity={self.item_quantity}))>'.format(self=self)


class ProductSchema(ItemSchema):
    @post_load()
    def make_product(self, data):
        return Product(**data)
