from app.singletons import db


class Product(db.Model):

    __tablename__ = 'product'

    code = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
