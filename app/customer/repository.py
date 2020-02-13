from app.singletons import db


class CustomerRepository:

    def read_all(self, customer):
        return customer.query.all()

    def read_one(self, code, customer):
        return customer.query.filter(customer.code == code).one_or_none()

    def create(self, customer):

        # Add the user to the database
        db.session.add(customer)
        db.session.commit()

    def update(self, existing_customer, updated_customer):

        # Set the id to the user we want to update
        updated_customer.code = existing_customer.code

        # merge the new object into the old and commit it to the db
        db.session.merge(updated_customer)
        db.session.commit()

    def delete(self, customer):

        db.session.delete(customer)
        db.session.commit()
