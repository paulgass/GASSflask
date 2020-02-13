from app.singletons import db


class UserRepository:

    def read_all(self, user):
        return user.query.all()

    def read_one(self, code, user):
        return user.query.filter(user.code == code).one_or_none()

    def create(self, user):

        # Add the user to the database
        db.session.add(user)
        db.session.commit()

    def update(self, existing_user, updated_user):

        # Set the id to the user we want to update
        updated_user.code = existing_user.code

        # merge the new object into the old and commit it to the db
        db.session.merge(updated_user)
        db.session.commit()

    def delete(self, user):

        db.session.delete(user)
        db.session.commit()
