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
- Total revenue generated from all customer orders across the platform, representing the overall financial performance of the marketplace.

**2. Total Orders (80,156)**
- Total number of successfully delivered orders, indicating overall customer demand and transaction volume.

**3. Total Products (32,951)**
- Total unique products available across all categories, reflecting the diversity of the product catalog.

**4. Average Order Value ($134.70)**
- Average revenue generated per order, providing insights into customer spending behavior and purchase value.

**5. Average Review Score (4.09)**
- Average customer rating across all completed orders, representing overall customer satisfaction with the shopping experience.

**6. Positive Review Rate (77.1%)**
- Percentage of orders receiving positive ratings (4 or 5 stars), indicating the quality of products and services delivered.

**7. On-Time Delivery Rate (89.9%)**
- Percentage of orders delivered on or before the estimated delivery date, measuring logistics and delivery performance.

**8. Average Delivery Days (14.38 Days)**
- Average time taken to deliver customer orders, providing insights into fulfillment efficiency and delivery speed.

**9. Total Sellers (3,095)**
- Total number of active sellers on the platform, representing the size of the marketplace's seller network.

**10. Average Freight Value ($23.45)**
- Average shipping cost charged per order, helping evaluate logistics expenses across product categories.

**11. Orders per Seller (24.44)**
- Average number of orders fulfilled by each seller, indicating seller productivity and marketplace activity.

**12. Average Quantity per Order (1.16)**
- Average number of products purchased in each order, providing insights into customer purchasing behavior and basket size.

**13. Total Customers (99,441)**
- Total number of unique customers who placed orders on the platform, representing the overall customer base.

**4. Active Customers (82,325)**
- Number of customers who successfully completed purchases, reflecting active user engagement within the marketplace.

**15. Customers per Seller (32.1)**
- Average number of customers served by each seller, measuring marketplace reach and seller demand.

**16. Customer-to-Seller Ratio (27.0)**
- Ratio of customers to sellers, indicating the balance between marketplace demand and supply.



___
<h2><a class="anchor" id="visual-analysis-breakdown"></a>Visual Analysis Breakdown and Business Impact</h2>

Each visual provides insights into different aspects of business performance, customer behavior, and operational efficiency.

## Visual Analysis Breakdown & Business Impact

### **1. Main Sales Trend**

- **What it shows:**
  - Displays monthly order trends across 2016, 2017, and 2018.
  - Highlights seasonal variations and year-over-year marketplace growth.

- **Key Insights:**
  - November 2017 recorded the highest monthly order volume.
  - 2018 started with stronger order volumes than previous years but declined after March.
  - Winter months experienced comparatively lower order activity.

- **Business Impact:**
  - Helps identify seasonal demand patterns for inventory and marketing planning.
  - Supports forecasting of future sales trends.
  - Enables businesses to align promotional campaigns with peak shopping periods.

---

### **2. Orders by Category (Pareto Analysis)**

- **What it shows:**
  - Compares order volume across major product categories.
  - Includes cumulative percentage contribution to total orders.

- **Key Insights:**
  - Home & Living contributes 31.1% of total orders.
  - Home & Living and Fashion & Beauty together account for 50.5% of all orders.
  - Only 38% of product subcategories generate more than half of total order volume.

- **Business Impact:**
  - Identifies the primary demand-driving product categories.
  - Helps optimize inventory allocation and category-level marketing investments.
  - Supports assortment planning by focusing on high-volume categories.
 

## Visual Analysis Breakdown & Business Impact

### **1. Review Distribution by Delivery Status**

- **What it shows:**
  - Compares review ratings for on-time and late deliveries.
  - Illustrates the relationship between delivery performance and customer satisfaction.

- **Key Insights:**
  - 5-star reviews dominate customer feedback.
  - Most positive reviews are associated with on-time deliveries.
  - Late deliveries contribute only a small proportion of total reviews.

- **Business Impact:**
  - Reinforces the importance of maintaining high on-time delivery performance.
  - Helps logistics teams understand the impact of delivery delays on customer satisfaction.
  - Supports initiatives aimed at improving fulfillment efficiency.

---

### **2. Average Review Score by Delivery Days**

- **What it shows:**
  - Displays average customer ratings based on delivery time intervals.

- **Key Insights:**
  - Orders delivered within 0–3 days receive the highest average rating (4.5).
  - Customer ratings decline as delivery time increases.
  - Deliveries exceeding 30 days receive the lowest average rating (2.2).

- **Business Impact:**
  - Quantifies the effect of delivery speed on customer experience.
  - Helps define delivery performance targets.
  - Supports investment in faster logistics and fulfillment operations.

---

### **3. Average Review Score by Product Category**

- **What it shows:**
  - Compares average customer ratings across major product categories.

- **Key Insights:**
  - Lifestyle & Entertainment and Daily Essentials achieve the highest average ratings (4.2).
  - All product categories maintain ratings above 4.0.
  - Customer satisfaction remains consistently high across categories.

- **Business Impact:**
  - Identifies categories delivering superior customer experiences.
  - Helps prioritize best-performing categories for promotional campaigns.
  - Supports quality improvement initiatives for comparatively lower-rated categories.

## Visual Analysis Breakdown & Business Impact

### **1. Payment Method Distribution**

- **What it shows:**
  - Displays the share of total orders by payment method.

- **Key Insights:**
  - Credit Cards account for 75.7% of all transactions.
  - Tickets represent 19.1% of orders.
  - Debit Cards contribute only 1.4%.

- **Business Impact:**
  - Helps optimize payment gateway strategies.
  - Identifies customer payment preferences.
  - Supports planning for payment-related promotions and partnerships.

---

### **2. Sales vs Average Freight Cost by Category**

- **What it shows:**
  - Compares total sales with average freight costs across product categories.

- **Key Insights:**
  - Home & Living generates the highest sales volume.
  - Automotive & Industrial records the highest average freight cost ($27.3).
  - Freight costs vary significantly across categories.

- **Business Impact:**
  - Identifies categories with high logistics expenses.
  - Supports freight cost optimization and pricing decisions.
  - Helps improve profitability through logistics planning.

---

### **3. Sellers & Average Order Value by State**

- **What it shows:**
  - Compares seller distribution and average order value across Brazilian states.

- **Key Insights:**
  - São Paulo hosts nearly 60% of sellers.
  - Bahia records the highest average order value despite having relatively few sellers.
  - Nineteen states outperform São Paulo in average order value.

- **Business Impact:**
  - Identifies underserved high-value markets.
  - Supports seller acquisition strategies by region.
  - Helps balance marketplace expansion across states.
 

## Visual Analysis Breakdown & Business Impact

### **1. Customer & Seller Landscape**

- **What it shows:**
  - Compares customers, sellers, and customer-to-seller ratio across product categories.

- **Key Insights:**
  - Home & Living and Fashion & Beauty have the largest customer base.
  - Electronics & Technology records the highest customer-to-seller ratio (27.5).
  - Other/Miscellaneous serves niche markets with lower customer demand.

- **Business Impact:**
  - Helps identify categories with demand-supply imbalances.
  - Supports onboarding of new sellers in high-demand categories.
  - Enables marketplace capacity planning.

---

### **2. Customer Behavior**

- **What it shows:**
  - Displays the proportion of one-time and repeat customers.

- **Key Insights:**
  - 94.7% of customers purchase only once.
  - Only 5.3% of customers make repeat purchases.

- **Business Impact:**
  - Highlights significant opportunities to improve customer retention.
  - Supports loyalty program and personalized marketing initiatives.
  - Helps reduce customer acquisition costs by increasing repeat purchases.

---

### **3. Average Orders per Customer by Category**

- **What it shows:**
  - Compares the average number of orders placed per customer across product categories.

- **Key Insights:**
  - Home & Living records the highest repeat purchase frequency.
  - Other/Miscellaneous has the lowest average orders per customer.
  - Customer purchasing behavior varies considerably across categories.

- **Business Impact:**
  - Identifies categories with stronger customer loyalty.
  - Helps design category-specific retention campaigns.
  - Supports cross-selling and upselling strategies.

---

### **4. Top 5 States by Customers**

- **What it shows:**
  - Displays the states contributing the highest number of customers.

- **Key Insights:**
  - São Paulo contributes over 41K customers.
  - Rio de Janeiro and Minas Gerais are the next largest customer markets.
  - The top five states account for the majority of the customer base.

- **Business Impact:**
  - Identifies key geographic markets driving customer demand.
  - Supports regional marketing and expansion strategies.
  - Helps prioritize customer acquisition efforts in high-value regions.



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
