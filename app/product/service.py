from app.product.models import Product
from app.product.schemas import ProductSchema
from app.product.repository import ProductRepository
from flask import abort, make_response

repository = ProductRepository()
product_schema = ProductSchema()
many_product_schema = ProductSchema(many=True)


class ProductService:

    def create(self, product):

        # Create a product level instance using the schema and the passed in json
        new_product = product_schema.load(product)

        # Determine if record with id exists
        existing_product = repository.read_one(code=new_product.code, product=Product)

        # Can we insert this record?
        if existing_product is None:

            # Add the object to the database
            repository.create(new_product)

            # Serialize and return the newly created object in the response
            data = product_schema.dump(new_product)

            return data, 201

        # Otherwise, nope, user exists already
        else:
            abort(409, f'product level with code {new_product.code} exists already')

    def update(self, code, product):

        # Determine if record with id exists
        existing_product = repository.read_one(code=code, product=Product)

        # Did we find an existing product level?
        if existing_product is not None:

            # Create an product level instance using the schema and the passed in product level
            updated_product = product_schema.load(product)

            # Update product in db
            repository.update(existing_product, updated_product)

            # return updated user in the response
            data = product_schema.dump(updated_product)

            return data, 200

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"User not found for Id: {code}")

    def delete(self, code):

        # Get the product level requested
        existing_product = repository.read_one(code, Product)

        # Did we find a product level?
        if existing_product is not None:
            repository.delete(existing_product)
            return make_response(f"User {code} deleted", 200)

        # Otherwise, nope, didn't find that product level
        else:
            abort(404, f"product level not found for Id: {code}")

    def get_by_id(self, code):

        # Determine if a product level with code exists
        existing_product = repository.read_one(code=code, product=Product)

        # Did we find a product level?
        if existing_product is not None:

            return product_schema.dump(existing_product)

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"product level not found for Id: {code}")

    def get_all(self):

        # Get all product level in db
        products = repository.read_all(Product)
        return many_product_schema.dump(products)
