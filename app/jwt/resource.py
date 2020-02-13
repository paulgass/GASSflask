from flask import request
from flask_restplus import Namespace, Resource, fields
from app.jwt.service import get_jwt_access_token

api = Namespace('jwt', description='JWT API')

model_jwt = api.model('JWT Model', {
    'username': fields.String(required=True, description="Username", help="username cannot be blank."),
    'password': fields.String(required=True, description="Password", help="password cannot be blank.")
    })

@api.route('')
class JWTResource(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(model_jwt)
    def post(self):
        try:
            json_string = request.json
            if not json_string:
                return {'message': 'No input data provided'}, 400
            return get_jwt_access_token(json_string['username'], json_string['password'])
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
