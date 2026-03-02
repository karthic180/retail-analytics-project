import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)

# Generate Customers
customers = []
for i in range(1000):
    customers.append({
        "customer_key": i+1,
        "customer_id": f"C{i+1000}",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "segment": random.choice(["Consumer","Corporate","Home Office"]),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "signup_date": fake.date_between(start_date='-3y', end_date='today')
    })

dim_customer = pd.DataFrame(customers)

# Generate Products
categories = {
    "Furniture": ["Chairs","Tables"],
    "Technology": ["Phones","Computers"],
    "Office Supplies": ["Paper","Binders"]
}

products = []
pk = 1
for cat, subs in categories.items():
    for sub in subs:
        for i in range(5):
            products.append({
                "product_key": pk,
                "product_id": f"P{pk+100}",
                "product_name": f"{sub} Item {i+1}",
                "category": cat,
                "subcategory": sub,
                "unit_price": random.randint(20,1500)
            })
            pk += 1

dim_product = pd.DataFrame(products)

# Generate Dates
dates = pd.date_range("2022-01-01","2025-12-31")
dim_date = pd.DataFrame({
    "full_date": dates
})
dim_date["date_key"] = dim_date["full_date"].dt.strftime("%Y%m%d").astype(int)
dim_date["year"] = dim_date["full_date"].dt.year
dim_date["quarter"] = "Q" + dim_date["full_date"].dt.quarter.astype(str)
dim_date["month"] = dim_date["full_date"].dt.month
dim_date["month_name"] = dim_date["full_date"].dt.month_name()
dim_date["day"] = dim_date["full_date"].dt.day

# Generate Sales
sales = []
for i in range(20000):
    product = dim_product.sample(1).iloc[0]
    quantity = random.randint(1,5)
    discount = random.choice([0,0.05,0.1,0.15])
    sales_amount = product.unit_price * quantity * (1-discount)
    profit = sales_amount * random.uniform(0.1,0.3)

    sales.append({
        "sales_key": i+1,
        "date_key": random.choice(dim_date["date_key"]),
        "customer_key": random.choice(dim_customer["customer_key"]),
        "product_key": product.product_key,
        "store_key": random.randint(1,3),
        "quantity": quantity,
        "discount": discount,
        "sales_amount": round(sales_amount,2),
        "profit": round(profit,2)
    })

fact_sales = pd.DataFrame(sales)

# Export CSVs
dim_customer.to_csv("dim_customer.csv", index=False)
dim_product.to_csv("dim_product.csv", index=False)
dim_date.to_csv("dim_date.csv", index=False)
fact_sales.to_csv("fact_sales.csv", index=False)