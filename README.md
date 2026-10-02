# Sales Analytics Dashboard

An interactive sales analytics project built using Python, Pandas, and Microsoft Power BI. The project focuses on data cleaning, exploratory analysis, business KPIs, data visualization, and interactive dashboard reporting.

## Project Overview

This project analyzes the Microsoft Financial Sample dataset to identify sales performance, profitability, product performance, country-level performance, customer segment performance, and yearly sales trends.

The project combines Python-based data preparation and analysis with Power BI dashboard development.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Microsoft Power BI
- Power Query
- DAX
- Git & GitHub

## Project Workflow

```text
Financial Sample Dataset
        ↓
Python + Pandas
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Data Visualization
        ↓
Power BI
        ↓
Power Query
        ↓
DAX Measures
        ↓
Interactive Dashboard
        ↓
Business Insights

Dataset

The project uses Microsoft's Financial Sample dataset.

The dataset contains sales and financial information including:

Segment
Country
Product
Discount Band
Units Sold
Manufacturing Price
Sale Price
Gross Sales
Discounts
Sales
COGS
Profit
Date
Month
Year
Data Cleaning

Python and Pandas were used to prepare the dataset.

The cleaning process included:

Loading the Excel dataset using Pandas
Cleaning column names
Checking duplicate records
Checking missing values
Handling missing Discount Band values
Converting the Date column
Creating Month and Quarter columns
Exporting the cleaned dataset to CSV

The cleaned dataset contains 700 records and 18 columns.

Key KPIs
KPI	Value
Total Sales	$118.73M
Total Profit	$16.89M
Total Units Sold	1,125,806
Total Records	700
Profit Margin	14.23%
Power BI Dashboard

The Power BI dashboard contains:

KPI cards
Sales by Product
Sales by Country
Sales by Segment
Sales Trend by Year
Profit by Product
Monthly Sales Trend
Sales vs Units Sold
Year filter
Country filter
Segment filter
Product filter
Sales Dashboard

Business Insights

Key Findings
Overall Performance

The dataset records $118.73M in total sales with a 14.23% overall profit margin.

Product Performance

Paseo recorded the highest sales among the products in the dataset, with approximately $33.01M in sales.

Country Performance

The United States of America recorded the highest sales among the countries, with approximately $25.03M in sales.

Segment Performance

The Government segment recorded the highest sales among the customer segments, with approximately $52.50M in sales.

Yearly Performance
2013 Sales: $26.42M
2014 Sales: $92.31M

Sales were substantially higher in 2014 than in 2013 in this dataset.

DAX Measures
Total Sales
Total Sales = SUM(cleaned_sales_data[Sales])
Total Profit
Total Profit = SUM(cleaned_sales_data[Profit])
Total Units Sold
Total Units Sold = SUM(cleaned_sales_data[Units Sold])
Total Records
Total Records = COUNTROWS(cleaned_sales_data)
Profit Margin
Profit Margin =
DIVIDE(
    [Total Profit],
    [Total Sales],
    0
)
Python Visualizations

The project also includes Python-generated visualizations for:

Sales by Product
Sales by Country
Sales by Segment
Sales by Year
Profit by Product
Monthly Sales Trend

The visualization files are available in the visualizations folder.

Project Structure
sales-analytics-dashboard/
│
├── screenshots/
│   ├── sales-dashboard.png
│   └── business-insights.png
│
├── visualizations/
│   ├── sales_by_product.png
│   ├── sales_by_country.png
│   ├── sales_by_segment.png
│   ├── sales_by_year.png
│   ├── profit_by_product.png
│   └── monthly_sales_trend.png
│
├── Financial Sample.xlsx
├── cleaned_sales_data.csv
├── Sales_Analytics_Dashboard.pbix
├── clean_sales_data.py
├── inspect_sales.py
├── sales_analysis.py
├── sales_visualizations.py
├── requirements.txt
├── README.md
└── .gitignore
Skills Demonstrated
Data Cleaning
Exploratory Data Analysis
Python Programming
Pandas
NumPy
Data Visualization
Matplotlib
Seaborn
Power BI
Power Query
DAX
Dashboard Development
Business Intelligence
Git
GitHub
Disclaimer

The analysis and findings in this project are based on Microsoft's Financial Sample dataset and are presented for educational and portfolio purposes. They should not be interpreted as current financial information about a real company.

Author

Dyanesh

BSc Computer Science