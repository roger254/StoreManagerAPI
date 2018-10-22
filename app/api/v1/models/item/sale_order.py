from marshmallow import post_load

from app.api.v1.models.item.item import Item, ItemSchema
from .item_type import ItemType


class SaleOrder(Item):
    """Represents the Sale Order"""

    def __init__(self, sale_name, sale_price, sale_quantity, created_by):
        self.item_type = ItemType.SALE_ORDER
        super(SaleOrder, self).__init__(sale_name, sale_price, sale_quantity, created_by)

    def __repr__(self):
        return '<SaleOrder(sale_name={self.item_name!r},' \
               ' sale_price={self.item_price!r},' \
               ' sale_quantity={self.item_quantity!r}, ' \
               'created_by={self.created_by!r}))>'.format(self=self)


class SaleOrderSchema(ItemSchema):
    @post_load()
    def make_sale(self, data):
        return SaleOrder(**data)
