# Sales Analytics Dashboard

An interactive sales analytics project built using Python, Pandas, and Microsoft Power BI. The project focuses on data cleaning, exploratory analysis, business KPIs, data visualization, and interactive dashboard reporting.

## Project Overview

This project analyzes the Microsoft Financial Sample dataset to identify sales performance, profitability, product performance, country-level performance, customer segment performance, and yearly sales trends.

The project combines Python-based data preparation with Power BI dashboard development.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Power BI
- Power Query
- DAX
- Excel
- Git & GitHub

## Project Workflow

Financial Sample Dataset
↓
Python + Pandas
↓
Data Cleaning
↓
Exploratory Data Analysis
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

## Dataset

Dataset: Microsoft Financial Sample

The dataset contains sales-related information including:

- Segment
- Country
- Product
- Units Sold
- Manufacturing Price
- Sale Price
- Gross Sales
- Discounts
- Sales
- COGS
- Profit
- Date
- Year

## Data Cleaning

Python and Pandas were used to:

- Clean column names
- Check duplicate records
- Handle missing values
- Convert date fields
- Create Month and Quarter columns
- Export the cleaned dataset to CSV

## Key KPIs

- Total Sales: $118.73M
- Total Profit: $16.89M
- Total Units Sold: 1,125,806
- Total Records: 700
- Profit Margin: 14.23%

## Dashboard Features

- Sales by Product
- Sales by Country
- Sales by Segment
- Sales Trend by Year
- Profit by Product
- Monthly Sales Trend
- Sales vs Units Sold
- Year filter
- Country filter
- Segment filter
- Product filter

## Key Findings

### Overall Performance

The dataset records $118.73M in total sales with a 14.23% overall profit margin.

### Product Performance

Paseo recorded the highest sales among the products in the dataset, with approximately $33.01M in sales.

### Country Performance

The United States of America recorded the highest sales among the countries, with approximately $25.03M in sales.

### Segment Performance

The Government segment recorded the highest sales among the customer segments, with approximately $52.50M in sales.

### Yearly Performance

- 2013 Sales: $26.42M
- 2014 Sales: $92.31M

Sales were substantially higher in 2014 than in 2013 in this dataset.

## DAX Measures

```DAX
Total Sales = SUM(cleaned_sales_data[Sales])
