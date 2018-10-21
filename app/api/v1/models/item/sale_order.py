from marshmallow import post_load

from app.api.v1.models.item.item import Item, ItemShema
from .item_type import ItemType
from app.api.v1.models.user.regular import Regular


class SaleOrder(Item):
    """Represents the Sale Order"""

    def __init__(self, sale_name, sale_price, sale_quantity, created_by):
        super(SaleOrder, self).__init__(sale_name, sale_price, sale_quantity, ItemType.SALE_ORDER)
        self.created_by = created_by

    def __repr__(self):
        return '<SaleOrder(sale_name={self.sale_name!r},' \
               ' sale_price={self.sale_price!r},' \
               ' sale_quantity={self.sale_quantity!r}, ' \
               'created_by={self.created_by!r}))>'.format(self=self)


class SaleOrderSchema(ItemShema):
    @post_load()
    def make_sale(self, data):
        return SaleOrder(**data)
