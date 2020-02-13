from flask import request
from flask_restplus import Namespace, Resource, fields
from app.customer.service import CustomerService

api = Namespace('customer', description='Rank  API')
service = CustomerService()

model_customer = api.model('Rank  Model', {
    'code': fields.String(required=True, description="code of the Rank ", help="code cannot be blank."),
    'description': fields.String(required=True, description="description of the Rank ", help="description cannot be blank.")
    })


@api.route('')
class CustomerListResource(Resource):

    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    def get(self):
        try:
            return service.get_all()
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(model_customer)
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


@api.route('/<int:customer_id>')
class CustomerResource(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'customer_id': 'Specify the transaction_id associated with the Rank '})
    def get(self, customer_id):
        try:
            return service.get_by_id(customer_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'customer_id': 'Specify the transaction_id associated with the Rank '})
    @api.expect(model_customer)
    def put(self, customer_id):
        try:
            json_data = request.json
            if not json_data:
                return {'message': 'No input data provided'}, 400

            return service.update(customer_id, json_data)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'customer_id': 'Specify the transaction_id associated with the Rank '})
    def delete(self, customer_id):
        try:
            return service.delete(customer_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
