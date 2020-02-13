from flask import request
from flask_restplus import Namespace, Resource, fields
from app.transaction.service import TransactionService
from app.bill.resource import model_bill
from app.product.resource import model_product
from app.customer.resource import model_customer
import os, sys
from datetime import datetime

api = Namespace('transactions', description='Transaction API')
service = TransactionService()

model_transaction = api.model('Transaction Model', {
    'transaction_id': fields.String(required=True, description="transaction ID of the Transaction", help="transaction_id cannot be blank."),
    'last_name': fields.String(required=True, description="Last Name of the Transaction", help="last_name cannot be blank."),
    'first_name': fields.String(required=True, description="First Name of the Transaction", help="first_name cannot be blank."),
    'bill': fields.Nested(model_bill, required = True, description="Bill  Nested List for the Transaction.", help="bill cannot be blank."),
    'product': fields.Nested(model_product, required = True, description="MOS  Nested List for the Transaction.", help="product cannot be blank."),
    'customer': fields.Nested(model_customer, required = True, description="Rank  Nested List for the Transaction.", help="customer cannot be blank."),
    'id': fields.String(required=True, description="ID of the Transaction", help="id cannot be blank."),
    'middle_initial': fields.String(required=True, description="Middle Initial of the Transaction", help="middle_initial cannot be blank."),
    'social_security_number': fields.String(required=True, description="Social Security Number of the Transaction", help="social_security_number cannot be blank."),
    'phone_number': fields.String(required=True, description="Phone Number of the Transaction", help="phone_number cannot be blank."),
    'dob': fields.Date(required=True, default='2000-01-31', description="Date Of Birth of the Transaction", help="dob cannot be blank."),
    'sex': fields.String(required=True, description="Sex of the Transaction", help="sex cannot be blank."),
    'active_service_date': fields.Date(required=True, default='2000-01-31', description="Active Service Date of the Transaction", help="active_service_date cannot be blank."),
    'arrival_date': fields.Date(required=True, default='2000-01-31', description="Arrival Date of the Transaction", help="arrival_date cannot be blank."),
    'dmsl': fields.String(required=True, description="DMSL of the Transaction", help="dmsl cannot be blank."),
    'gt_score': fields.String(required=True, description="GT Score of the Transaction", help="gt_score cannot be blank."),
    'contract_acquistion': fields.String(required=True, description="Contract Aquisition of the Transaction", help="contract_acquistion cannot be blank."),
    'emergency_contact_first_name': fields.String(required=True, description="Emergency Contact First Name of the Transaction", help="emergency_contact_first_name cannot be blank."),
    'emergency_contact_last_name': fields.String(required=True, description="Emergency Contact Last Name of the Transaction", help="emergency_contact_last_name cannot be blank."),
    'emergency_contact_phone_number': fields.String(required=True, description="Emergency Contact Phone Number of the Transaction", help="emergency_contact_phone_number cannot be blank."),
    'emergency_contact_relationship': fields.String(required=True, description="Emergency Contact Relationship of the Transaction", help="emergency_contact_relationship cannot be blank."),
    'time_standard': fields.String(required=True, description="Time Standard of the Transaction", help="time_standard cannot be blank."),
    'attended': fields.Boolean(required=True, description="True or False for the Attendance status of the Transaction", help="attended cannot be blank."),
    'failure_code': fields.String(required=True, description="Failure Code of the Transaction", help="failure_code cannot be blank."),
    'failure_comment': fields.String(required=True, description="Failure Comment of the Transaction", help="failure_comment cannot be blank."),
    'home_of_record': fields.String(required=True, description="Home of Record of the Transaction", help="home_of_record cannot be blank."),
    'arrived_from': fields.String(required=True, description="Arrived From of the Transaction", help="arrived_from cannot be blank."),
    'has_dependents': fields.Boolean(required=True, description="True or False for the Dependents status of the Transaction", help="has_dependents cannot be blank."),
    'ranger_regiment_discovered': fields.String(required=True, description="Ranger Regiment Discovered of the Transaction", help="ranger_regiment_discovered cannot be blank."),
    'is_tdy': fields.Boolean(required=True, description="True or False for the TDY status of the Transaction", help="is_tdy cannot be blank."),
    'tdy_unit': fields.String(required=True, description="TDY Unit of the Transaction", help="tdy_unit cannot be blank."),
    'played_sports': fields.Boolean(required=True, description="True or False for the Played Sports status of the Transaction", help="played_sports cannot be blank."),
    'sports_played': fields.String(required=True, description="Sports Played of the Transaction", help="sports_played cannot be blank."),
    'has_hot_weather_injury': fields.Boolean(required=True, description="True or False for the Hot Weather Injury status of the Transaction", help="has_hot_weather_injury cannot be blank."),
    'has_cold_weather_injury': fields.Boolean(required=True, description="True or False for the Cold Weather Injury status of the Transaction", help="has_cold_weather_injury cannot be blank."),
    'has_physical': fields.Boolean(required=True, description="True or False for the Physical status of the Transaction", help="has_physical cannot be blank."),
    'has_airborne': fields.Boolean(required=True, description="True or False for the Airborne status of the Transaction", help="has_airborne cannot be blank."),
    'has_ranger_sof_affiliations': fields.Boolean(required=True, description="True or False for the Ranger SOF Affiliations status of the Transaction", help="has_ranger_sof_affiliations cannot be blank."),
    'has_glasses': fields.Boolean(required=True, description="True or False for the Glasses status of the Transaction", help="has_glasses cannot be blank."),
    'success_factors': fields.String(required=True, description="Success Factors of the Transaction", help="success_factors cannot be blank."),
    'success_motivators': fields.String(required=True, description="Success Motivators of the Transaction", help="success_motivators cannot be blank."),
    'bad_habits': fields.String(required=True, description="Bad Habits of the Transaction", help="bad_habits cannot be blank.")
})

@api.route('')
class TransactionListResource(Resource):

    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    def get(self):
        try:
            return service.get_all()
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(model_transaction)
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


@api.route('/<int:transaction_id>')
class TransactionResource(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'transaction_id': 'Specify the transaction_id associated with the transaction'})
    def get(self, transaction_id):
        try:
            return service.get_by_id(transaction_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'transaction_id': 'Specify the transaction_id associated with the transaction'})
    @api.expect(model_transaction)
    def put(self, transaction_id):
        try:
            json_data = request.json
            if not json_data:
                return {'message': 'No input data provided'}, 400

            return service.update(transaction_id, json_data)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'transaction_id': 'Specify the transaction_id associated with the transaction'})
    def delete(self, transaction_id):
        try:
            return service.delete(transaction_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

