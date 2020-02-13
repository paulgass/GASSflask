from app.singletons import db


class ProductRepository:

    def read_all(self, product):
        return product.query.all()

    def read_one(self, code, product):
        return product.query.filter(product.code == code).one_or_none()

    def create(self, product):

        # Add the user to the database
        db.session.add(product)
        db.session.commit()

    def update(self, existing_product, updated_product):

        # Set the id to the user we want to update
        updated_product.code = existing_product.code

        # merge the new object into the old and commit it to the db
        db.session.merge(updated_product)
        db.session.commit()

    def delete(self, product):

        db.session.delete(product)
        db.session.commit()
