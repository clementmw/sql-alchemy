from sqlalchemy import create_engine,desc
from sqlalchemy import (Column,DateTime,Integer,String)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine  = create_engine('sqlite:///hotel.db')


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    price = Column(Integer())

def __repr__(self):
        return f"restaurant  {self.id}: " \
            + f"{self.name}, " \
            + f"{self.price}"

class Customer(Base):
      __tablename__ = 'customers'

      id  = Column(Integer(), primary_key= True)
      first_name = Column(String())
      last_name = Column(String())

def __repr__(self):
        return f"customer {self.id}: " \
            + f"first name {self.first_name}, " \
            + f" last name {self.last_name}"

