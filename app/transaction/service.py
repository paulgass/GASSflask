from app.transaction.models import Transaction
from app.transaction.schemas import TransactionSchema
from app.transaction.repository import TransactionRepository
from flask import abort, make_response

repository_transaction = TransactionRepository()
schema_transaction = TransactionSchema()
many_schema_transaction = TransactionSchema(many=True)


class TransactionService:

    def create(self, transaction_json):

        # Create a transaction instance using the schema and the passed in transaction
        new_transaction = schema_transaction.load(transaction_json)

        # Determine if record with id exists
        existing_transaction = repository_transaction.read_one(transaction_id=new_transaction.transaction_id, transaction=Transaction)

        # Can we insert this record?
        if existing_transaction is None:

            # Add the object to the database
            repository_transaction.create(new_transaction)

            # Serialize and return the newly created object in the response
            data = schema_transaction.dump(new_transaction)

            return data, 201

        # Otherwise, nope, user exists already
        else:
            abort(409, f'Transaction with transaction ID {new_transaction.transaction_id} exists already')

    def update(self, transaction_id, transaction_json):

        # Determine if record with id exists
        existing_transaction = repository_transaction.read_one(transaction_id=transaction_id, transaction=Transaction)

        # Did we find an existing transaction?
        if existing_transaction is not None:

            # Create a transaction instance using the schema and the passed in transaction
            updated_transaction = schema_transaction.load(transaction_json)

            # Update transaction in db
            repository_transaction.update(existing_transaction, updated_transaction)

            # return updated user in the response
            data = schema_transaction.dump(updated_transaction)

            return data, 200

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"User not found for Id: {transaction_id}")

    def delete(self, transaction_id):

        # Get the transaction requested
        existing_transaction = Transaction.query.filter(Transaction.transaction_id == transaction_id).one_or_none()

        # Did we find a transaction?
        if existing_transaction is not None:
            repository_transaction.delete(existing_transaction)
            return make_response(f"User {transaction_id} deleted", 200)

        # Otherwise, nope, didn't find that transaction
        else:
            abort(404, f"Transaction not found for Id: {transaction_id}")

    def get_by_id(self, transaction_id):

        # Determine if a transaction with id exists
        existing_transaction = repository_transaction.read_one(transaction_id=transaction_id, transaction=Transaction)

        # Did we find a transaction?
        if existing_transaction is not None:

            return  schema_transaction.dump(existing_transaction)

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"transaction not found for Id: {transaction_id}")

    def get_all(self):

        # Get all transactions in db
        transactions = repository_transaction.read_all(Transaction)
        return many_schema_transaction.dump(transactions)
