from app.customer.models import Customer
from app.customer.schemas import CustomerSchema
from app.customer.repository import CustomerRepository
from flask import abort, make_response

repository = CustomerRepository()
customer_schema = CustomerSchema()
many_customer_schema = CustomerSchema(many=True)


class CustomerService:

    def create(self, customer):

        # Create a customer level instance using the schema and the passed in json
        new_customer = customer_schema.load(customer)

        # Determine if record with id exists
        existing_customer = repository.read_one(code=new_customer.code, customer=Customer)

        # Can we insert this record?
        if existing_customer is None:

            # Add the object to the database
            repository.create(new_customer)

            # Serialize and return the newly created object in the response
            data = customer_schema.dump(new_customer)

            return data, 201

        # Otherwise, nope, user exists already
        else:
            abort(409, f'customer level with code {new_customer.code} exists already')

    def update(self, code, customer):

        # Determine if record with id exists
        existing_customer = repository.read_one(code=code, customer=Customer)

        # Did we find an existing customer level?
        if existing_customer is not None:

            # Create an customer level instance using the schema and the passed in customer level
            updated_customer = customer_schema.load(customer)

            # Update customer in db
            repository.update(existing_customer, updated_customer)

            # return updated user in the response
            data = customer_schema.dump(updated_customer)

            return data, 200

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"User not found for Id: {code}")

    def delete(self, code):

        # Get the customer level requested
        existing_customer = repository.read_one(code, Customer)

        # Did we find a customer level?
        if existing_customer is not None:
            repository.delete(existing_customer)
            return make_response(f"User {code} deleted", 200)

        # Otherwise, nope, didn't find that customer level
        else:
            abort(404, f"customer level not found for Id: {code}")

    def get_by_id(self, code):

        # Determine if a customer level with code exists
        existing_customer = repository.read_one(code=code, customer=Customer)

        # Did we find a customer level?
        if existing_customer is not None:

            return customer_schema.dump(existing_customer)

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"customer level not found for Id: {code}")

    def get_all(self):

        # Get all customer level in db
        customers = repository.read_all(Customer)
        return many_customer_schema.dump(customers)
