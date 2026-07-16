# ORDERS and REVIEWS
'''
    Description:
    This script connects to SQL Server, extracts Orders, Payments, Order Items, 
    and Reviews data from OLIST e-commerce database, performs data cleaning,
    data validation, and transformation, and prepares the data for analysis
    and dashboarding in Power BI.
'''


# IMPORTING LIBRARIES
import numpy as np
import pandas as pd
import pyodbc
from unidecode import unidecode
import re




# CREATING DATABASE CONNECTION

# Defining SQL Server Name (Enter your own SERVER NAME here)
server = r"ARSHIT_BHARDWAJ\SQLEXPRESS01"

# Defining Database Name (Enter the database present on your server, in which olist dataset is present)
database = "Olist"   

# Create connection string to connect Python with SQL Server
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

# Establish connection to SQL Server
conn = pyodbc.connect(connection_string)




# EXTRACTING ORDERS TABLE

# Fetch orders dataset from SQL Server
query = "SELECT  * FROM olist_orders_dataset"

# Load data into Pandas DataFrame
orders= pd.read_sql(query, conn)


# Convert columns to datetime format
date_cols = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]
for c in date_cols:
    orders[c] = pd.to_datetime(orders[c], errors='coerce', infer_datetime_format=True)



# REMOVE INVALID DATE RECORDS

# Remove records where approval is before purchase
# Remove records where carrier delivery is before approval
orders = orders[
    ((orders['order_approved_at'] - orders['order_purchase_timestamp']).dt.total_seconds()/86400 >= 0) &
    ((orders['order_delivered_carrier_date'] - orders['order_approved_at']).dt.days >= 0)
]

# Remove canceled orders that still show delivery
to_remove = orders[(orders['order_delivered_customer_date'].notna()) & 
                         (orders["order_status"] == "canceled")].index

orders= orders.drop(to_remove)




# EXTRACTING ORDERS TABLE

# Fetch payments dataset from SQL Server
query= "select * from olist_order_payments_dataset"

# Load data into Pandas DataFrame
payments= pd.read_sql(query, conn)

# Remove unnecessary columns
payments.drop(columns=["payment_sequential"], inplace=True)
payments.drop(columns=["payment_installments"], inplace=True)

# Aggregate payments by order and payment type
payments= payments.groupby(["order_id","payment_type"]).sum("payment_value").reset_index()

# Merge payments with orders dataset
orders= pd.merge(orders, payments, on="order_id", how="inner")




# EXTRACTING ORDER_ITEMS TABLE

# Fetch orders_items dataset from SQL Server
query= "select * from olist_order_items_dataset"

# Load data into Pandas DaataFrame
olist_items= pd.read_sql(query, conn)

# Merge with orders dataset
orders= pd.merge(orders, olist_items, on="order_id", how="left")

# Keep only valid shipping records
orders=  orders[
    (orders["shipping_limit_date"] > orders["order_purchase_timestamp"]) &
    (orders["shipping_limit_date"] > orders["order_approved_at"]) &
    (orders["shipping_limit_date"] < orders["order_delivered_customer_date"])
]
orders.sort_values(by=["order_item_id","order_id"], ascending=False)

# Remove unnecessary column
orders.drop(columns="order_item_id", inplace=True)

# Aggregate order items
orders= orders.groupby(['order_id', 'customer_id', 'order_status', 'order_purchase_timestamp',
       'order_approved_at', 'order_delivered_carrier_date',
       'order_delivered_customer_date', 'order_estimated_delivery_date',
       'payment_type', 'payment_value', 'product_id', 'seller_id',
       'shipping_limit_date']).agg(price=("price", "sum"),
                                   freight_value=("freight_value", "sum"),
                                   quantity=("product_id","count")).reset_index()




# EXTRACTING ORDER_REVIEWS TABLE

# Fetch orders_reviews dataset from SQL Server
query="select * from olist_order_reviews_dataset"

# Load data into Pandas DataFrame
reviews= pd.read_sql(query, conn)

# Keep only reviews for valid orders
reviews= reviews[reviews["order_id"].isin(orders["order_id"])]

# Remove unnecessary column
reviews.drop(columns="review_comment_title", inplace=True)

# Convert review answer timestamp to date only
reviews['review_answer_timestamp'] = reviews['review_answer_timestamp'].dt.date
