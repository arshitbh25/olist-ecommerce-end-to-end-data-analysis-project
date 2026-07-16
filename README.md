# 🛒 RetailIQ: E-Commerce Sales and Customer Analytics

This project presents a comprehensive end-to-end data analysis of the OLIST e-commerce dataset to understand sales performance, customer behavior, delivery efficiency, and revenue trends using SQL Server, Python, and Power BI. The project demonstrates a complete industry-style data workflow including data storage, cleaning, transformation, and dashboard development.

___
## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#tech-stack">Tech Stack Used</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#datasource">Data Source</a>
- <a href="#features">Features of the Report</a>
- <a href="#er-diagram">Relationship Diagram (Power BI)</a>
- <a href="#snapshot">Snapshot</a>
- <a href="#kpis">Key KPIs</a>
- <a href="#visual-analysis-breakdown">Visual Analysis Breakdown and Business Impact</a>
- <a href="#conclusion">Conclusion</a>
- <a href="#author--contact">Author and Contact</a>


___
<h2><a class="anchor" id="overview"></a>Overview</h2>

This project simulates a real-world data analyst workflow by building a complete data pipeline from raw data ingestion to dashboard visualization.

The workflow includes:
- Downloading raw Excel datasets from Kaggle
- Importing raw data into SQL Server for structured storage
- Extracting and transforming data using Python and Pandas
- Cleaning and validating messy and inconsistent records
- Loading processed data into Power BI
- Creating an interactive dashboard to analyze business performance

The goal of this project is to generate meaningful insights related to sales, customers, products, and operational efficiency.


___
<h2><a class="anchor" id="tech-stack"></a>Tech Stack Used</h2>

**Database & Storage :**
- Microsoft SQL Server

**Programming & Data Processing :**
- Python
  - Pandas
  - NumPy
  - PyODBC
  - Unidecode
  - Regex

**Data Visualization :**
- Power BI Desktop

**Other Tools :**
- Excel
- Kaggle


___
<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
olist-ecommerce-end-to-end-data-analysis/
|
├── data/
|   ├── dataset_information.pdf
|   ├── olist_customers_dataset.csv
|   ├── olist_geolocation_dataset.csv
|   ├── olist_order_items_dataset.csv
|   ├── olist_order_payments_dataset.csv
|   ├── olist_order_reviews_dataset.csv
|   ├── olist_orders_dataset.csv
|   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   └── product_category_name_translation.csv
|
├── images/
│   ├── 00_data_model.png
│   ├── 01_exclusive_overview.png
│   ├── 02_customer_&_product_insights.png
│   ├── 03_operations_&_seller_performance.png
│   └── 04_customer_experience.png
|
├── report/
│   └── olist_e_commerce_performance dashboard.pbix
|
├── scripts/
│   ├── clean_customers.py
│   ├── clean_geolocation.py
│   ├── clean_orders_reviews.py
│   └── clean_products_sellers.py
|
├── .gitattributes
|
└── README.me
```



___
<h2><a class="anchor" id="datasource"></a>Data Source</h2>

**Dataset :** Brazilian E-Commerce Public Dataset by Olist
```bash
└── data/
     ├── olist_customers_dataset.csv
     ├── olist_geolocation_dataset.csv
     ├── olist_order_items_dataset.csv
     ├── olist_order_payments_dataset.csv
     ├── olist_order_reviews_dataset.csv
     ├── olist_orders_dataset.csv
     ├── olist_products_dataset.csv
     ├── olist_sellers_dataset.csv
     └── product_category_name_translation.csv
```

**Source :** Kaggle
This dataset contains real transactional data from an e-commerce platform, including:
- Customers
- Orders
- Products
- Sellers
- Payments
- Reviews
- Geolocation

Dataset characteristics:
- Multiple relational tables
- Real-world messy and inconsistent data
- Missing values and duplicates
- Timestamp-based transactional records

This dataset is ideal for performing real-world data cleaning, transformation, and analysis.



___
<h2><a class="anchor" id="features"></a>Features of the Report</h2>

- End-to-end data pipeline implementation
- Data storage using SQL Server
- Data extraction using Python and SQL connection
- Data cleaning using Pandas
- Removal of invalid and inconsistent records
- Handling missing values and formatting issues
- Data transformation and aggregation
- Interactive Power BI dashboard
- Multi-page dashboard with filters and slicers



___
<h2><a class="anchor" id="er-diagram"></a>Relationship Diagram (Power BI - Data Model)</h2>

![ER-Diagram](https://github.com/arshitbh25/olist-ecommerce-end-to-end-data-analysis-project/blob/main/images/00_data_model.png)



___
<h2><a class="anchor" id="snapshot"></a>Snapshot</h2>

**Exclusive Overview**
![Dashboard Preview](https://github.com/arshitbh25/olist-ecommerce-end-to-end-data-analysis-project/blob/main/images/01_exclusive_overview.png)

**Customer & Product Insights**
![Dashboard Preview](https://github.com/arshitbh25/olist-ecommerce-end-to-end-data-analysis-project/blob/main/images/02_customer_%26_product_insights.png)

**Operations & Seller Performance**
![Dashboard Preview](https://github.com/arshitbh25/olist-ecommerce-end-to-end-data-analysis-project/blob/main/images/03_operations_%26_seller_performance.png)

**Customer Experience**
![Dashboard Preview](https://github.com/arshitbh25/olist-ecommerce-end-to-end-data-analysis-project/blob/main/images/04_customer_experience.png)




___
<h2><a class="anchor" id="kpis"></a>Key KPIs</h2>

**1. Total Sales ($10.8M)**
- Total revenue generated from all customer orders across the platform, representing overall business financial performance.

**2. Total Orders (80.16K)**
- Total number of orders placed by customers, indicating overall transaction volume and platform usage.

**3. Total Customers (75.65K)**
- Total number of unique customers who placed at least one order, representing the platform’s customer base size.

**4. Total Products (32.95K)**
- Total number of distinct products sold on the platform, reflecting product diversity and catalog scale.

**5. Average Order Value ($142.72)**
- Average revenue generated per order, measuring customer spending behavior and revenue efficiency.

**6. Inactive Customers (17.12K)**
- Number of customers who have stopped purchasing from last 6 months, highlighting customer churn and retention challenges.

**7. Churned Customers (23,788)**
- Total customers who became inactive during the analyzed period, representing potential revenue loss risk.



___
<h2><a class="anchor" id="visual-analysis-breakdown"></a>Visual Analysis Breakdown and Business Impact</h2>

Each visual provides insights into different aspects of business performance, customer behavior, and operational efficiency.

**1. Category Contribution to Total Sales**
- What it shows:
  - Displays the percentage contribution of each product category to total revenue.
- Key Insights:
  - Top category: watches_gifts contributes 9.18%
  - health_beauty contributes 9.12%
  - bed_bath_table contributes 7.92%
- Business Impact:
  - Top 3 categories contribute over 26% of total revenue ($2.8M+)
  - Helps prioritize high-performing categories for marketing and inventory optimization.
 

**2. Main Sales Trend (Monthly Order Trend)**
- What it shows:
  - Tracks monthly order volume trends across years.
- Key Insights:
  - Significant growth observed in late-year months.
  - Peak order volume exceeds 6K orders per month
- Business Impact:
  - Indicates strong seasonal demand patterns.
  - Helps forecast inventory and staffing requirements.
 

**3. Payment Type Distribution**
- What it shows:
  - Distribution of revenue across different payment methods.
- Key Insights:
  - Credit Card: $10.34M (78.56%)
  - Boleto: $2.37M (17.97%)
  - Others contribute minimal share.
- Business Impact:
  - Over 78% dependency on credit cards
  - Ensures focus on secure and optimized credit card payment systems.
 

**4. Delivery Performance (Review Score vs Delivery Status)**
- What it shows:
  - Average customer review scores based on delivery timeliness.
- Key Insights:
  - On-time delivery review score: 4.26
  - Late delivery review score: 2.56
- Business Impact:
  - Late deliveries reduce customer satisfaction by ~40%
  - Improving delivery efficiency can significantly improve customer retention.
 

**5. Average Fulfillment Time by Order Stage**
- What it shows:
  - Time taken at each stage of order fulfillment.
- Key Insights:
  - Stage	Time (Average) :
    - Order Approval	9.59 hours
    - Shipping	74.97 hours
    - Delivery	262.12 hours
- Business Impact:
  - Delivery stage accounts for ~75% of total fulfillment time
  - Major optimization opportunity in logistics and delivery operations.
 

**6. Product Sales Performance (First 90 Days vs Last 90 Days)**
- What it shows:
  - Compares product sales performance between early and later lifecycle stages.
- Key Insights:
  - Total sales increase: $1,942,608
  - Top category increase: health_beauty ($254K)
- Business Impact:
  - Shows strong product adoption and growth.
  - Helps identify high-growth product categories.
 

**7. New Product Performance (Orders vs Sales by Category)**
- What it shows:
  - Tracks performance of newly launched products across categories.
- Key Insights:
  - Top performing category generated over $220K in sales
  - Multiple categories show consistent demand.
- Business Impact:
  - Helps identify successful product launches.
  - Supports product expansion strategy.
 

**8. Poor Performing Sellers Analysis**
- What it shows:
  - Identifies sellers with low performance metrics.
- Key Insights:
  - Poor sellers handled 262 orders
  - Average review score still high at 4.56
  - Local sales contribution only 3.82%
- Business Impact:
  - Identifies underperforming sellers for performance improvement.
  - Improves marketplace quality and customer experience.
 

**9. Customer Order Behavior vs Price Change**
- What it shows:
  - Impact of price changes on customer ordering behavior.
- Key Insights:
  - Price changes caused demand fluctuations up to ±200%
- Business Impact:
  - Helps optimize pricing strategy.
  - Prevents revenue loss due to improper pricing.
 

**10. Market Basket Analysis**

- What it shows:
  - Product combinations frequently purchased together.
- Key Insights:
  - Maximum lift value: 70.64
  - Indicates strong product association patterns.
- Business Impact:
  - Helps in cross-selling and bundling strategies.
  - Increases average order value and revenue.



___
<h2><a class="anchor" id="conclusion"></a>Conclusion</h2>

This project demonstrates a complete end-to-end data analysis workflow using industry-standard tools.

Key achievements
- Built structured data storage using SQL Server
- Performed data cleaning and transformation using Python
- Created an interactive dashboard using Power BI
- Generated actionable business insights

This project showcases strong skills in:
- Data Cleaning
- Data Transformation
- Data Analysis
- Dashboard Development
- End-to-End Data Pipeline

___
<h2><a class="anchor" id="author--contact"></a>Author and Contact</h2>

**Arshit Bhardwaj**  
Aspiring Data Analyst

📧 Email: arshitbh25@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/arshit-bhardwaj/)  
🔗 [Portfolio](https://arshitbhardwaj.edgeone.app/)
