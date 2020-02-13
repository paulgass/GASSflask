from app.user.models import User
from app.user.schemas import UserSchema
from app.user.repository import UserRepository
from flask import abort, make_response

repository = UserRepository()
user_schema = UserSchema()
many_user_schema = UserSchema(many=True)


class UserService:

    def create(self, user):

        # Create a user level instance using the schema and the passed in json
        new_user = user_schema.load(user)

        # Determine if record with id exists
        existing_user = repository.read_one(code=new_user.code, user=User)

        # Can we insert this record?
        if existing_user is None:

            # Add the object to the database
            repository.create(new_user)

            # Serialize and return the newly created object in the response
            data = user_schema.dump(new_user)

            return data, 201

        # Otherwise, nope, user exists already
        else:
            abort(409, f'user level with code {new_user.code} exists already')

    def update(self, code, user):

        # Determine if record with id exists
        existing_user = repository.read_one(code=code, user=User)

        # Did we find an existing user level?
        if existing_user is not None:

            # Create an user level instance using the schema and the passed in user level
            updated_user = user_schema.load(user)

            # Update user in db
            repository.update(existing_user, updated_user)

            # return updated user in the response
            data = user_schema.dump(updated_user)

            return data, 200

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"User not found for Id: {code}")

    def delete(self, code):

        # Get the user level requested
        existing_user = repository.read_one(code, User)

        # Did we find a user level?
        if existing_user is not None:
            repository.delete(existing_user)
            return make_response(f"User {code} deleted", 200)

        # Otherwise, nope, didn't find that user level
        else:
            abort(404, f"user level not found for Id: {code}")

    def get_by_id(self, code):

        # Determine if a user level with code exists
        existing_user = repository.read_one(code=code, user=User)

        # Did we find a user level?
        if existing_user is not None:

            return user_schema.dump(existing_user)

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"user level not found for Id: {code}")

    def get_all(self):

        # Get all user level in db
        users = repository.read_all(User)
        return many_user_schema.dump(users)
