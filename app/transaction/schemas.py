from marshmallow import Schema, fields, post_load
from app.transaction.models import Transaction
from app.bill.schemas import BillSchema
from app.product.schemas import ProductSchema
from app.customer.schemas import CustomerSchema


class TransactionSchema(Schema):

    transaction_id = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    bill = fields.Nested(BillSchema)
    product = fields.Nested(ProductSchema)
    customer = fields.Nested(CustomerSchema)
    id = fields.String()
    middle_initial = fields.String()
    social_security_number = fields.String()
    phone_number = fields.String()
    dob = fields.Date()
    sex = fields.String()
    active_service_date = fields.Date()
    arrival_date = fields.Date()
    dmsl = fields.String()
    gt_score = fields.String()
    contract_acquistion = fields.String()
    emergency_contact_first_name = fields.String()
    emergency_contact_last_name = fields.String()
    emergency_contact_phone_number = fields.String()
    emergency_contact_relationship = fields.String()
    time_standard = fields.String()
    attended = fields.Boolean()
    failure_code = fields.String()
    failure_comment = fields.String()
    datetime_creation = fields.DateTime()
    datetime_update = fields.DateTime()
    home_of_record = fields.String()
    arrived_from = fields.String()
    has_dependents = fields.Boolean()
    ranger_regiment_discovered = fields.String()
    is_tdy = fields.Boolean()
    tdy_unit = fields.String()
    played_sports = fields.Boolean()
    sports_played = fields.String()
    has_hot_weather_injury = fields.Boolean()
    has_cold_weather_injury = fields.Boolean()
    has_physical = fields.Boolean()
    has_airborne = fields.Boolean()
    has_ranger_sof_affiliations = fields.Boolean()
    has_glasses = fields.Boolean()
    success_factors = fields.String()
    success_motivators = fields.String()
    bad_habits = fields.String()

    @post_load
    def make_transaction(self, data, **kwargs):
        return Transaction(**data)
