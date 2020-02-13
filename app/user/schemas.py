from marshmallow import Schema, fields, post_load
from app.user.models import User


class UserSchema(Schema):

    code = fields.String()
    description = fields.String()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
