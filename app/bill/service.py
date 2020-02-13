from app.bill.models import Bill
from app.bill.schemas import BillSchema
from app.bill.repository import BillRepository
from flask import abort, make_response

repository = BillRepository()
bill_schema = BillSchema()
many_bill_schema = BillSchema(many=True)


class BillService:

    def create(self, bill):

        # Create a bill level instance using the schema and the passed in json
        new_bill = bill_schema.load(bill)

        # Determine if record with id exists
        existing_bill = repository.read_one(code=new_bill.code, bill=Bill)

        # Can we insert this record?
        if existing_bill is None:

            # Add the object to the database
            repository.create(new_bill)

            # Serialize and return the newly created object in the response
            data = bill_schema.dump(new_bill)

            return data, 201

        # Otherwise, nope, user exists already
        else:
            abort(409, f'bill level with code {new_bill.code} exists already')

    def update(self, code, bill):

        # Determine if record with id exists
        existing_bill = repository.read_one(code=code, bill=Bill)

        # Did we find an existing bill level?
        if existing_bill is not None:

            # Create an bill level instance using the schema and the passed in bill level
            updated_bill = bill_schema.load(bill)

            # Update bill in db
            repository.update(existing_bill, updated_bill)

            # return updated user in the response
            data = bill_schema.dump(updated_bill)

            return data, 200

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"User not found for Id: {code}")

    def delete(self, code):

        # Get the bill level requested
        existing_bill = repository.read_one(code, Bill)

        # Did we find a bill level?
        if existing_bill is not None:
            repository.delete(existing_bill)
            return make_response(f"User {code} deleted", 200)

        # Otherwise, nope, didn't find that bill level
        else:
            abort(404, f"bill level not found for Id: {code}")

    def get_by_id(self, code):

        # Determine if a bill level with code exists
        existing_bill = repository.read_one(code=code, bill=Bill)

        # Did we find a bill level?
        if existing_bill is not None:

            return bill_schema.dump(existing_bill)

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"bill level not found for Id: {code}")

    def get_all(self):

        # Get all bill level in db
        bills = repository.read_all(Bill)
        return many_bill_schema.dump(bills)
