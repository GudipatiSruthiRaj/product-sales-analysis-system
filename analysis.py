import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# ---------- connect to MySQL ----------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your password",          # your password here
    database="sales_db"
)

# ---------- load all tables into dataframes ----------
df_sales    = pd.read_sql("SELECT * FROM sales", conn)
df_products = pd.read_sql("SELECT * FROM products", conn)
df_customers= pd.read_sql("SELECT * FROM customers", conn)

print("Data loaded successfully!")
print(f"Sales shape    : {df_sales.shape}")
print(f"Products shape : {df_products.shape}")
print(f"Customers shape: {df_customers.shape}")

# ---------- merge into one master dataframe ----------
df = df_sales.merge(df_products, on="product_id") \
             .merge(df_customers, on="customer_id")

print(f"\nMaster dataframe shape: {df.shape}")
print(df.head())

# ---------- basic analysis ----------
print("\n--- Business Insights ---")

# 1. Total revenue
print(f"Total Revenue : ₹{df['total_amount'].sum():,.2f}")

# 2. Average order value
print(f"Avg Order Value: ₹{df['total_amount'].mean():,.2f}")

# 3. Best category
best_cat = df.groupby('category')['total_amount'].sum().idxmax()
print(f"Best Category : {best_cat}")

# 4. Best product
best_prod = df.groupby('product_name')['total_amount'].sum().idxmax()
print(f"Best Product  : {best_prod}")

# 5. Best region
best_region = df.groupby('region')['total_amount'].sum().idxmax()
print(f"Best Region   : {best_region}")

# ---------- chart 1: revenue by category ----------
plt.figure(figsize=(10, 5))
df.groupby('category')['total_amount'].sum().sort_values().plot(kind='barh', color='steelblue')
plt.title('Revenue by Category')
plt.xlabel('Total Revenue (₹)')
plt.tight_layout()
plt.savefig('chart1_category_revenue.png')
plt.show()
print("Chart 1 saved!")

# ---------- chart 2: monthly revenue trend ----------
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['month'] = df['sale_date'].dt.to_period('M')
plt.figure(figsize=(12, 5))
df.groupby('month')['total_amount'].sum().plot(kind='line', marker='o', color='green')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue (₹)')
plt.tight_layout()
plt.savefig('chart2_monthly_trend.png')
plt.show()
print("Chart 2 saved!")

# ---------- chart 3: top 10 products ----------
plt.figure(figsize=(10, 6))
df.groupby('product_name')['total_amount'].sum().nlargest(10).sort_values().plot(
    kind='barh', color='coral')
plt.title('Top 10 Products by Revenue')
plt.xlabel('Total Revenue (₹)')
plt.tight_layout()
plt.savefig('chart3_top_products.png')
plt.show()
print("Chart 3 saved!")

# ---------- chart 4: revenue by region ----------
plt.figure(figsize=(8, 5))
df.groupby('region')['total_amount'].sum().plot(kind='bar', color='purple', rot=0)
plt.title('Revenue by Region')
plt.ylabel('Total Revenue (₹)')
plt.tight_layout()
plt.savefig('chart4_region_revenue.png')
plt.show()
print("Chart 4 saved!")

conn.close()
print("\nAll done! 4 charts saved.")
