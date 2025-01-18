from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here

class Earthquake(db.models,SerializerMixin):
    __tablename__ = "earthquakes"
    id = db.Column(db.Integer,primary_key = True)
    magnitute = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Eartquake {self.id}, {self.magnitute}, {self.location}, {self.year}>"

