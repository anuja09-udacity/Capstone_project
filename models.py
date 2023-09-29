import os
import json
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy

#for Render
#database_path= 'postgres://castingagency_w28h_user:JdAoxlf1xEmdXkG3HRXRASNAVhFnrqYr@dpg-ck88ajfsasqs73c5ost0-a/castingagency_w28h'

#for testing locally
database_user = os.environ.get('db_user')
database_pwd = os.environ.get('db_pwd')
database_name = "castingagency"
database_path = "postgresql://{}:{}@{}/{}".format(
    database_user, database_pwd, "localhost:5432", database_name)

db = SQLAlchemy()

#print ('db user', database_user)

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def create_tables():
    db.create_all()


'''
Movie
Have title and release year
'''
class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_year = Column(Integer)
    actors = db.relationship('Actor', backref='movies')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year
        }

'''
Actor
'''

class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    movie_id = db.Column(
        db.Integer,
        db.ForeignKey('movies.id'),
        nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movie_id': self.movie_id
        }