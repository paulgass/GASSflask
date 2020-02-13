from marshmallow import Schema, fields, post_load
from app.bill.models import Bill


class BillSchema(Schema):

    code = fields.String()
    description = fields.String()

    @post_load
    def make_bill(self, data, **kwargs):
        return Bill(**data)
