# PRODUCTS and SELLERS
'''
    Description:
    This script extracts products and sellers data from SQL Server,
    performs cleaning, standardizes product categories, merges
    category translation, and prepares the data for analysis and Power BI.
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



# EXTRACTING PRODUCTS TABLE

# Fetch products dataset from SQL Server
query = "SELECT * FROM olist_products_dataset"

# Load data into Pandas DataFrame
products = pd.read_sql(query, conn)




# REMOVE UNNECESSARY COLUMNS

# Drop columns not required for analysis or dashboard
# These columns relate to dimensions and description length,
# which are not currently used for business insights
products.drop(columns=['product_name_lenght',
       'product_description_lenght', 'product_weight_g',
       'product_length_cm', 'product_height_cm', 'product_width_cm'], inplace=True)



# LOAD CATEGORY TRANSLATION TABLE
# Fetch category translation table
query = "SELECT * FROM product_category_name_translation"

# Load into DataFrame
product_name = pd.read_sql(query, conn)



# MERGE PRODUCTS WITH TRANSLATION TABLE

# Merge to replace Portuguese category names with English names
products= pd.merge(products, product_name, on= "product_category_name", how="left")



# Replace incorrect or unclear category names manually

# Fix pc_gamer category
products.loc[
    products["product_category_name"] == "pc_gamer",
    "product_category_name_english"
] = "computers"

# Fix kitchen appliance category
products.loc[
    products["product_category_name"] == "portateis_cozinha_e_preparadores_de_alimentos",
    "product_category_name_english"
] = "small_appliances_home_oven_and_coffee"



# FINALIZE PRODUCT CATEGORY COLUMN

# Replace original category column with translated category
products["product_category_name"]=products["product_category_name_english"]

# Remove temporary translation columns
products.drop(columns=['product_category_name_english'], inplace=True)






# EXTRACTING SELLERS TABLE

# Fetch sellers dataset from SQL Server
query = "SELECT * FROM olist_sellers_dataset"

# Load into DataFrame
seller = pd.read_sql(query, conn)

# Convert seller city names into Title Case
seller["seller_city"]= seller["seller_city"].str.title()