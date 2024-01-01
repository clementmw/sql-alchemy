from faker import Faker 
from sqlalchemy.orm import sessionmaker

from models import engine,Base,Restaurant,Customer,Review

fake = Faker() #to create a faker instance

Session = sessionmaker(bind=engine)
session  = Session()

#seed data for restraurant

restaurants = [
    Restaurant(name = fake.company(), 
               price = fake.random_int(min=1, max=5)
               )
for i in range(5)
]
session.add_all(restaurants)

#seed data for customer
customers = [
    Customer(first_name = fake.first_name(),
             last_name = fake.last_name()
             )
for i in range(5)
]
session.add_all(customers)

#seed data for reviews
reviews  =[
    Review(star_rating = fake.random_int(min=1, max=5),
           customer = fake.random_element(customers),
           restaurant = fake.random_element(restaurants)

           )
for i in range(5)
]
session.add_all(reviews)

session.commit()