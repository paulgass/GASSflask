from flask import request
from flask_restplus import Namespace, Resource, fields
from app.product.service import ProductService
from app.authentication import authenticate

api = Namespace('product', description='MOS  API')
service = ProductService()

model_product = api.model('MOS  Model', {
    'code': fields.String(required=True, description="code of the MOS ", help="code cannot be blank."),
    'description': fields.String(required=True, description="description of the MOS ", help="description cannot be blank.")
    })


@api.route('')
class ProductListResource(Resource):

    @authenticate
    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    def get(self):
        try:
            return service.get_all()
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(model_product)
    def post(self):
        try:

            json_string = request.json
            if not json_string:
                return {'message': 'No input data provided'}, 400

            return service.create(json_string)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


@api.route('/<int:product_id>')
class ProductResource(Resource):

    method_decorators = [authenticate]

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'product_id': 'Specify the transaction_id associated with the MOS '})
    def get(self, product_id):
        try:
            return service.get_by_id(product_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'product_id': 'Specify the transaction_id associated with the MOS '})
    @api.expect(model_product)
    def put(self, product_id):
        try:
            json_data = request.json
            if not json_data:
                return {'message': 'No input data provided'}, 400

            return service.update(product_id, json_data)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'product_id': 'Specify the transaction_id associated with the MOS '})
    def delete(self, product_id):
        try:
            return service.delete(product_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
