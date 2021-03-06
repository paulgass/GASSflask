from app.singletons import db


class User(db.Model):

    __tablename__ = 'user'

    code = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
