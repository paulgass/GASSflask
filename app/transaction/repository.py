from app.singletons import db


class TransactionRepository:

    def read_all(self, transaction):
        return transaction.query.all()

    def read_one(self, transaction_id, transaction):
        return transaction.query.filter(transaction.transaction_id == transaction_id).one_or_none()

    def create(self, transaction):

        # Add the user to the database
        db.session.add(transaction)
        db.session.commit()

    def update(self, existing_transaction, updated_transaction):

        # Set the id to the user we want to update
        updated_transaction.transaction_id = existing_transaction.transaction_id

        # merge the new object into the old and commit it to the db
        db.session.merge(updated_transaction)
        db.session.commit()

    def delete(self, transaction):

        db.session.delete(transaction)
        db.session.commit()
