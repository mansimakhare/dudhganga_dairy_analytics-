import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# --- 1. CONFIGURATION ---
# Let's define how much data we want
NUM_CUSTOMERS = 500
NUM_PRODUCTS = 20
NUM_ORDERS = 1500

# Initialize the Faker library
fake = Faker('en_IN') # Using Indian locale for more relevant names/addresses

# --- 2. DEFINE YOUR PRODUCTS ---
# Let's create a realistic list of dairy products
product_list = [
    {'name': 'Toned Milk (1L)', 'category': 'Milk', 'price': 50},
    {'name': 'Full Cream Milk (1L)', 'category': 'Milk', 'price': 60},
    {'name': 'Paneer (200g)', 'category': 'Value-Add', 'price': 80},
    {'name': 'Ghee (500g)', 'category': 'Value-Add', 'price': 250},
    {'name': 'Curd (400g)', 'category': 'Curd & Yogurt', 'price': 40},
    {'name': 'Butter (100g)', 'category': 'Value-Add', 'price': 55},
    {'name': 'Lassi (200ml)', 'category': 'Drinks', 'price': 25},
    {'name': 'Cheese Slices (10 pack)', 'category': 'Value-Add', 'price': 120},
    {'name': 'Flavored Milk (200ml)', 'category': 'Drinks', 'price': 30},
    {'name': 'Dahi (500g)', 'category': 'Curd & Yogurt', 'price': 60},
    {'name': 'Skimmed Milk (1L)', 'category': 'Milk', 'price': 55},
    {'name': 'Makkhan (Butter) (500g)', 'category': 'Value-Add', 'price': 250},
    {'name': 'Probiotic Yogurt (150g)', 'category': 'Curd & Yogurt', 'price': 45},
    {'name': 'Chocolate Milk (200ml)', 'category': 'Drinks', 'price': 35},
    {'name': 'Cheese Block (200g)', 'category': 'Value-Add', 'price': 150},
    {'name': 'Lassi with Fruit (200ml)', 'category': 'Drinks', 'price': 30},
    {'name': 'Dahi with Fruit (500g)', 'category': 'Curd & Yogurt', 'price': 70},
    {'name': 'Toned Milk (500ml)', 'category': 'Milk', 'price': 25},
    {'name': 'Full Cream Milk (500ml)', 'category': 'Milk', 'price': 30},
    {'name': 'Paneer Cubes (200g)', 'category': 'Value-Add', 'price': 90}
]

# --- 3. GENERATE DATA ---

# A) Generate Customers
print("Generating customers...")
customers = []
for i in range(NUM_CUSTOMERS):
    customers.append({
        'customer_id': 1001 + i,
        'name': fake.name(),
        'city': fake.city(),
        'signup_date': fake.date_between(start_date='-2y', end_date='today')
    })
customers_df = pd.DataFrame(customers)


# B) Generate Products
print("Generating products...")
# Let's add a product_id to our list
for i, prod in enumerate(product_list):
    prod['product_id'] = 201 + i
products_df = pd.DataFrame(product_list)


# C) Generate Orders
print("Generating orders...")
orders = []
# Get lists of possible customer and product IDs to choose from
customer_ids = customers_df['customer_id'].tolist()
product_ids = products_df['product_id'].tolist()

for i in range(NUM_ORDERS):
    # Choose a random customer and product
    cust_id = random.choice(customer_ids)
    prod_id = random.choice(product_ids)
    
    # Get the customer's signup date to make sure order date is after signup
    signup_date = customers_df.loc[customers_df['customer_id'] == cust_id, 'signup_date'].iloc[0]
    
    orders.append({
        'order_id': 5001 + i,
        'customer_id': cust_id,
        'product_id': prod_id,
        'order_date': fake.date_between(start_date=signup_date, end_date='today'),
        'quantity': random.randint(1, 5) # Customer buys between 1 and 5 items
    })
orders_df = pd.DataFrame(orders)

# --- 4. SAVE TO CSV ---
print("Saving files to CSV...")
customers_df.to_csv('customers.csv', index=False)
products_df.to_csv('products.csv', index=False)
orders_df.to_csv('orders.csv', index=False)

print("Data generation complete! 3 files created.")