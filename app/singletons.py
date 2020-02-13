from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'authorization'
    }
}

api = Api(
    title='Transaction API',
    version='1.0',
    description='Transaction API',
    authorizations=authorizations,
    security='apikey',
)

db = SQLAlchemy()
ma = Marshmallow()
