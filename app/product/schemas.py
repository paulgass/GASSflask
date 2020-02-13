from marshmallow import Schema, fields, post_load
from app.product.models import Product


class ProductSchema(Schema):

    code = fields.String()
    description = fields.String()

    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data)
