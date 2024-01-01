from sqlalchemy import create_engine,desc,ForeignKey
from sqlalchemy import (Column,DateTime,Integer,String)
from sqlalchemy.orm import (sessionmaker,relationship)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine  = create_engine('sqlite:///hotel.db')


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    price = Column(Integer())

    #to establish a connection to reviews
    reviews  = relationship('Review',backref = 'restaurant')

def __repr__(self):
        return f"restaurant  {self.id}: " \
            + f"{self.name}, " \
            + f"{self.price}"

class Customer(Base):
      __tablename__ = 'customers'

      id  = Column(Integer(), primary_key= True)
      first_name = Column(String())
      last_name = Column(String())

      reviews = relationship('Review',backref = 'customer')

    

def __repr__(self):
        return f"customer {self.id}: " \
            + f"first name {self.first_name}, " \
            + f" last name {self.last_name}"


class Review (Base):
       __tablename__ = 'reviews'

       id = Column(Integer(), primary_key = True)
       star_rating = Column(Integer())

       #establish relationship to both restaurant and customer
       restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
       customer_id = Column(Integer(), ForeignKey('customers.id'))

def __repr__(self):
        return f"review {self.id}: " \
            + f"{self.star_rating}, " 
           