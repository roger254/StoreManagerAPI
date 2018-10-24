from app.api.v1.models.items.item import Item
from app.api.v1.models.items.item_type import ItemType


class Product(Item):
    """Represents the Store Attendant"""

    def __init__(self, p_id, p_name, p_price, p_quantity):
        super(Product, self).__init__(p_id, p_name, p_price, p_quantity, 'PRODUCT')
