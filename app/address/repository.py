from app.singletons import db


class AddressRepository:

    def read_all(self, address):
        return address.query.all()

    def read_one(self, code, address):
        return address.query.filter(address.code == code).one_or_none()

    def create(self, address):

        # Add the user to the database
        db.session.add(address)
        db.session.commit()

    def update(self, existing_address, updated_address):

        # Set the id to the user we want to update
        updated_address.code = existing_address.code

        # merge the new object into the old and commit it to the db
        db.session.merge(updated_address)
        db.session.commit()

    def delete(self, address):

        db.session.delete(address)
        db.session.commit()
