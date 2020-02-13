from app.singletons import db


class Address(db.Model):

    __tablename__ = 'address'

    code = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
