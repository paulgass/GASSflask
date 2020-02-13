from app.singletons import db


class BillRepository:

    def read_all(self, bill):
        return bill.query.all()

    def read_one(self, code, bill):
        return bill.query.filter(bill.code == code).one_or_none()

    def create(self, bill):

        # Add the user to the database
        db.session.add(bill)
        db.session.commit()

    def update(self, existing_bill, updated_bill):

        # Set the id to the user we want to update
        updated_bill.code = existing_bill.code

        # merge the new object into the old and commit it to the db
        db.session.merge(updated_bill)
        db.session.commit()

    def delete(self, bill):

        db.session.delete(bill)
        db.session.commit()
