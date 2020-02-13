from app.address.models import Address
from app.address.schemas import AddressSchema
from app.address.repository import AddressRepository
from flask import abort, make_response

repository = AddressRepository()
address_schema = AddressSchema()
many_address_schema = AddressSchema(many=True)


class AddressService:

    def create(self, address):

        # Create a address level instance using the schema and the passed in json
        new_address = address_schema.load(address)

        # Determine if record with id exists
        existing_address = repository.read_one(code=new_address.code, address=Address)

        # Can we insert this record?
        if existing_address is None:

            # Add the object to the database
            repository.create(new_address)

            # Serialize and return the newly created object in the response
            data = address_schema.dump(new_address)

            return data, 201

        # Otherwise, nope, user exists already
        else:
            abort(409, f'address level with code {new_address.code} exists already')

    def update(self, code, address):

        # Determine if record with id exists
        existing_address = repository.read_one(code=code, address=Address)

        # Did we find an existing address level?
        if existing_address is not None:

            # Create an address level instance using the schema and the passed in address level
            updated_address = address_schema.load(address)

            # Update address in db
            repository.update(existing_address, updated_address)

            # return updated user in the response
            data = address_schema.dump(updated_address)

            return data, 200

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"User not found for Id: {code}")

    def delete(self, code):

        # Get the address level requested
        existing_address = repository.read_one(code, Address)

        # Did we find a address level?
        if existing_address is not None:
            repository.delete(existing_address)
            return make_response(f"User {code} deleted", 200)

        # Otherwise, nope, didn't find that address level
        else:
            abort(404, f"address level not found for Id: {code}")

    def get_by_id(self, code):

        # Determine if a address level with code exists
        existing_address = repository.read_one(code=code, address=Address)

        # Did we find a address level?
        if existing_address is not None:

            return address_schema.dump(existing_address)

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"address level not found for Id: {code}")

    def get_all(self):

        # Get all address level in db
        addresss = repository.read_all(Address)
        return many_address_schema.dump(addresss)
