from app.singletons import db


class Customer(db.Model):

    __tablename__ = 'customer'

    code = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
