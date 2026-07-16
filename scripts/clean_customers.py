# CUSTOMERS
'''
    Description:
    This script connects to SQL Server, extracts the customers table,
    performs data cleaning, and prepares it for further analysis
    and visualization in Power BI.
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




# EXTRACTING CUSTOMERS TABLE


# SQL query to fetch all records from customers table
query = "SELECT  * FROM olist_customers_dataset;"

# Load SQL query result into Pandas DataFrame
customers= pd.read_sql(query, conn)



# DATA CLEANING - CUSTOMER CITY COLUMN

# Remove unnecessary column to reduce redundancy
customers.drop(columns="customer_unique_id", inplace=True)




# REMOVE ACCENTS

customers["customer_city"]= customers["customer_city"].apply(lambda x: unidecode(x))




# FUNCTION TO REMOVE EVERYTHING EXCEPT TEXT

def keep_only_text(x):
    
    if pd.isna(x):
        return x

    #  removes everything except space or text
    return re.sub(r"[^A-Za-z\s]","",str(x)).strip()




# REMOVE EVERY UNNCESSARY CHARACTER FROM CITY NAMES EXCEPT TEXT

customers["customer_city"]= customers["customer_city"].apply(keep_only_text)



# Convert city names to Title Case
customers["customer_city"]=customers["customer_city"].str.title()