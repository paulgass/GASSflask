from marshmallow import Schema, fields, post_load
from app.address.models import Address


class AddressSchema(Schema):

    code = fields.String()
    description = fields.String()

    @post_load
    def make_address(self, data, **kwargs):
        return Address(**data)
