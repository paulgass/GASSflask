from app.singletons import db


class Bill(db.Model):

    __tablename__ = 'bill'

    code = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
