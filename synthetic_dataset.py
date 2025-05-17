from faker import Faker 
import pandas as pd 
import numpy as np 
import random

random.seed(42)

faker = Faker()
# Synthetic Dataset being created !!!
num_of_customers = 2000
data = []

for i in range(num_of_customers):
    customer_id = faker.uuid4()
    gender = random.choice(["Male","Female"])
    age = random.randint(18,65)
    country = faker.country()
    pages_visited = random.randint(1,20)
    session_time = round(random.uniform(1.5,30.0),2)
    purchased = random.choice([0,1])
    product_clicked = faker.word()
    product_category = random.choice(["Electronics", "Clothing", "Books", "Home", "Beauty"])
    price = round(random.uniform(5.0, 500.0), 2) if purchased else 0

    data.append([customer_id, gender, age, country, pages_visited, session_time, purchased, product_clicked, product_category, price])


df = pd.DataFrame(data, columns=['customer_id', 'gender', 'age', 'country', 'pages_visited',
    'session_time', 'purchased', 'product_clicked',
    'product_category', 'price'])

df.to_csv("synthetic_ecommerce_data.csv", index=False)
