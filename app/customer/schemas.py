from marshmallow import Schema, fields, post_load
from app.customer.models import Customer


class CustomerSchema(Schema):

    code = fields.String()
    description = fields.String()

    @post_load
    def make_customer(self, data, **kwargs):
        return Customer(**data)
