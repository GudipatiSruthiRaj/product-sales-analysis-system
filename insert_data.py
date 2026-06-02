import mysql.connector
import random
from datetime import date, timedelta

# ---------- connect to your MySQL ----------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sruthi123",   # <-- change this
    database="sales_db"
)
cursor = conn.cursor()

# ---------- sample data ----------
products = [
    ("iPhone 15",        "Electronics",   79999),
    ("Samsung Galaxy",   "Electronics",   59999),
    ("Dell Laptop",      "Electronics",  145000),
    ("HP Laptop",        "Electronics",   89000),
    ("Sony Headphones",  "Electronics",   12999),
    ("Nike Shoes",       "Clothing",       8999),
    ("Adidas T-Shirt",   "Clothing",       2499),
    ("Levi's Jeans",     "Clothing",       3999),
    ("Whirlpool Fridge", "Appliances",    45000),
    ("LG Washing Mach",  "Appliances",    38000),
    ("Bajaj Mixer",      "Appliances",     4500),
    ("Prestige Cooker",  "Kitchen",        2999),
    ("Bosch Microwave",  "Kitchen",       12500),
    ("Cricket Bat",      "Sports",         3500),
    ("Football",         "Sports",         1299),
    ("yoga Mat",         "Sports",          899),
    ("Harry Potter",     "Books",           599),
    ("Atomic Habits",    "Books",           450),
    ("Python Crash Crs", "Books",           799),
    ("Face Wash",        "Beauty",          349),
]

cities_regions = [
    ("Hyderabad", "South"), ("Chennai",   "South"),
    ("Bangalore", "South"), ("Mumbai",    "West"),
    ("Pune",      "West"),  ("Delhi",     "North"),
    ("Jaipur",    "North"), ("Lucknow",   "North"),
    ("Kolkata",   "East"),  ("Bhubaneswar","East"),
]

first_names = ["Ravi","Priya","Arjun","Sneha","Kiran","Meera",
               "Rahul","Divya","Suresh","Anita","Vikram","Pooja",
               "Amit","Kavya","Rohit","Lakshmi","Nikhil","Sita"]
last_names  = ["Kumar","Sharma","Reddy","Singh","Patel","Naidu",
               "Verma","Rao","Joshi","Mehta","Iyer","Nair"]

# ---------- insert products ----------
cursor.executemany(
    "INSERT INTO products (product_name, category, price) VALUES (%s, %s, %s)",
    products
)
print(f"Inserted {len(products)} products")

# ---------- insert 300 customers ----------
customers = []
for _ in range(300):
    name = random.choice(first_names) + " " + random.choice(last_names)
    city, region = random.choice(cities_regions)
    customers.append((name, city, region))

cursor.executemany(
    "INSERT INTO customers (customer_name, city, region) VALUES (%s, %s, %s)",
    customers
)
print(f"Inserted {len(customers)} customers")

# ---------- insert 5000 sales ----------
def random_date():
    start = date(2023, 1, 1)
    return start + timedelta(days=random.randint(0, 730))  # 2 years of data

sales = []
for _ in range(5000):
    product_id  = random.randint(1, len(products))
    customer_id = random.randint(1, 300)
    quantity    = random.randint(1, 5)
    price       = products[product_id - 1][2]
    total       = round(price * quantity, 2)
    sale_date   = random_date()
    sales.append((product_id, customer_id, quantity, sale_date, total))

cursor.executemany(
    """INSERT INTO sales
       (product_id, customer_id, quantity, sale_date, total_amount)
       VALUES (%s, %s, %s, %s, %s)""",
    sales
)
print(f"Inserted {len(sales)} sales records")

# ---------- done ----------
conn.commit()
cursor.close()
conn.close()
print("\nAll done! Database has 5,000+ records ready.")