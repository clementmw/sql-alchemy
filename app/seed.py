from faker import Faker
from sqlalchemy import desc,func
from sqlalchemy.orm import sessionmaker
from models import engine, Base, Restaurant, Customer, Review

fake = Faker()  # Create a Faker instance

Session = sessionmaker(bind=engine)
session = Session()

#clear existing data 
session.query(Restaurant).delete()
session.query(Customer).delete()
session.query(Review).delete()

session.commit() # commit changes to the db 

# Seed data for restaurants
restaurants = [
    Restaurant(name=fake.company(), 
               price=fake.random_int(min=1, max=5))
    for _ in range(5)
]
session.add_all(restaurants)

# Seed data for customers
customers = [
    Customer(first_name=fake.first_name(),
             last_name=fake.last_name())
    for _ in range(5)
]
session.add_all(customers)

# Seed data for reviews
reviews = [
    Review(star_rating=fake.random_int(min=1, max=5),
           customer=fake.random_element(customers),
           restaurant=fake.random_element(restaurants))
    for _ in range(5)
]
session.add_all(reviews)

session.commit()



# Get reviews

get_reviews = session.query(Review).all()

for review in get_reviews:
    customer = review.customer
    restaurant = review.restaurant
    print(f"review {review.id}:  {customer.first_name}, Restaurant: {restaurant.name}")



# Get all restaurants and print their reviews and customers

all_restaurants = session.query(Restaurant).all()
        # print (f"{all_restaurants}")

for restaurant in all_restaurants:
    for review in restaurant.reviews:
        print(f"Restaurant: {restaurant.name} , Rating: {review.star_rating}, Customer :{review.customer.first_name}")


# Get all customers and print their reviews       
all_customers = session.query(Customer).all()
for customer in all_customers:
    for review in customer.reviews:
        print(f"Customer: {customer.first_name} , Restaurant: {review.restaurant.name}")

#get full name using concat
full_name = session.query (func.concat(Customer.first_name,' ',Customer.last_name).label('full_name')).all()

for name in full_name:
    print(name.full_name)

session.close()
