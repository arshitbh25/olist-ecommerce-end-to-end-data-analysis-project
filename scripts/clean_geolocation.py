# GEOLOCATION
'''
    Description:
    This script connects to SQL Server, extracts the geolocation table,
    performs data cleaning on city names, removes unnecessary columns,
    and prepares the dataset for further analysis and visualization.
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




# EXTRACTING GEOLOCATION TABLE


# SQL query to fetch geolocation dataset
query = "SELECT * FROM olist_geolocation_dataset"

# Load SQL data into Pandas DataFrame
geo = pd.read_sql(query, conn)




# FUNCTION TO REMOVE EVERYTHING EXCEPT TEXT

def keep_only_text(x):
    
    if pd.isna(x):
        return x

    #  removes everything except space or text
    return re.sub(r"[^A-Za-z\s]","",str(x)).strip()


# REMOVE EVERY UNNCESSARY CHARACTER FROM CITY NAMES EXCEPT TEXT

geo["geolocation_city"]= geo["geolocation_city"].apply(keep_only_text)



# Remove latitude and longitude columns
    # Reason: Not required for current dashboard analysis
geo.drop(columns=["geolocation_lat", "geolocation_lng"], inplace=True)

# Remove special accented characters
geo["geolocation_city"]= geo["geolocation_city"].apply(lambda x: unidecode(x))

# Convert city names to Title Case
geo['geolocation_city'] = geo['geolocation_city'].str.title()