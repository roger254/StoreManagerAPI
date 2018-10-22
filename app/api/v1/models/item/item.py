import datetime as date
from marshmallow import Schema, fields


class Item:
    """Represents The Item Model"""
    item_type = None

    def __init__(self, item_name, item_price, item_quantity, created_by):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.created_by = created_by
        self.date_created = date.datetime.now()

    def __repr__(self):
        return '<Item(item_name={self.item_name!r}, ' \
               'item_price={self.item_price}, ' \
               'item_quantity={self.item_quantity})>'.format(self=self)


# to serialize and deserialize user from and to json obj
class ItemSchema(Schema):
    """ Represents Fields for Item"""
    item_name = fields.Str()
    item_price = fields.Float()
    item_quantity = fields.Int()
    date_created = fields.Date()
    created_by = fields.Str()
