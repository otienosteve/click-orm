from sqlalchemy import Integer, String, Column, ForeignKey, create_engine, Table
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

movie_directors = Table('movie_directors',
                        Base.metadata,
                        Column('movie_id',ForeignKey('movies.id')),
                        Column('director_id',ForeignKey('directors.id')),
                        extend_existing=True)

class Movie(Base):
    __tablename__="movies"
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    photo_url = Column(String(70))
    user_id = Column(Integer,ForeignKey('users.id'))
    directors = relationship('Director', secondary=movie_directors,back_populates='movies')

class Director(Base):
    __tablename__="directors"
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    movies = relationship('Movie', secondary=movie_directors, back_populates='directors')

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    email =Column(String(40))
    movies = relationship('Movie', backref='user')

engine = create_engine('sqlite:///movie.db')
Session = sessionmaker(bind=engine)

# Base.metadata.create_all(bind=engine)
session = Session()