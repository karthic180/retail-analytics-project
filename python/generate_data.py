import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
np.random.seed(42)

# Date dimension
start_date = datetime(2022, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(730)]

dim_date = pd.DataFrame({
    "date": dates,
    "year": [d.year for d in dates],
    "month": [d.month for d in dates],
    "month_name": [d.strftime("%B") for d in dates],
    "quarter": [(d.month - 1) // 3 + 1 for d in dates]
})

dim_date.to_csv("python/dim_date.csv", index=False)

# Product dimension
products = []
categories = ["Electronics", "Clothing", "Home", "Sports"]

for i in range(1, 51):
    products.append([
        i,
        f"Product_{i}",
        np.random.choice(categories),
        round(np.random.uniform(10, 500), 2)
    ])

dim_product = pd.DataFrame(products, columns=[
    "product_id", "product_name", "category", "cost"
])

dim_product.to_csv("python/dim_product.csv", index=False)

# Customer dimension
customers = []

for i in range(1, 201):
    customers.append([
        i,
        fake.name(),
        np.random.choice(["Consumer", "Corporate", "Small Business"]),
        fake.state()
    ])

dim_customer = pd.DataFrame(customers, columns=[
    "customer_id", "customer_name", "segment", "state"
])

dim_customer.to_csv("python/dim_customer.csv", index=False)

# Fact table
sales = []

for i in range(10000):
    product = np.random.choice(dim_product["product_id"])
    customer = np.random.choice(dim_customer["customer_id"])
    date = np.random.choice(dim_date["date"])
    quantity = np.random.randint(1, 5)
    price = float(dim_product.loc[dim_product["product_id"] == product, "cost"])
    revenue = quantity * price * np.random.uniform(1.1, 1.5)

    sales.append([
        date,
        product,
        customer,
        quantity,
        round(revenue, 2)
    ])

fact_sales = pd.DataFrame(sales, columns=[
    "date", "product_id", "customer_id", "quantity", "sales_amount"
])

fact_sales.to_csv("python/fact_sales.csv", index=False)

print("Synthetic retail data generated successfully.")