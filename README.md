
# 📊 Retail Sales Analytics & Forecasting Platform

An end-to-end Business Intelligence project simulating a real-world retail analytics environment using dimensional modeling, DAX, and Power BI.

---

## 🚀 Executive Summary

This project demonstrates the design and implementation of a modern BI solution for a retail company. 

The objective was to:

- Analyze sales and profitability performance
- Identify high-performing products and customer segments
- Implement a star schema data model
- Apply time intelligence calculations
- Forecast future revenue trends

The solution includes synthetic data engineering, dimensional modeling, and executive-level dashboard design.

---

## 🏗️ Architecture Overview

### 🔹 Data Generation Layer
Synthetic retail data generated using Python.

### 🔹 Data Modeling Layer
Star schema design:

**Fact Table**
- `fact_sales`

**Dimension Tables**
- `dim_customer`
- `dim_product`
- `dim_date`

**Grain:**  
One row per product per transaction per day.

---

## 📊 Dashboard Pages

### 1️⃣ Executive Overview
- Total Sales
- Total Profit
- Profit Margin %
- YoY Growth
- Sales Trend with Forecast

### 2️⃣ Product Insights
- Top 10 Products by Revenue
- Product Performance Table
- Margin Conditional Formatting
- Contribution % Analysis

### 3️⃣ Customer Analytics
- Sales by Segment
- Regional Performance
- Customer Count
- Average Order Value

---

## 📈 Key DAX Measures

- Total Sales
- Total Profit
- Profit Margin %
- Year-over-Year Growth
- Cumulative Sales
- Product % of Total
- Average Order Value

---

## 🔮 Forecasting

Power BI’s built-in time-series forecasting was applied to sales trend data to project future performance.

---

## 📷 Dashboard Preview

### Executive Overview
![Executive Dashboard](screenshots/executive.png)

### Product Insights
![Product Insights](screenshots/product.png)

### Customer Analytics
![Customer Analytics](screenshots/customer.png)

### Star Schema Model
![Star Schema](screenshots/model.png)

---

## 📄 Full Power BI Report

Download the complete exported report:

👉 [Download Full Report (PDF)](reports/Retail-Analytics-Report.pdf)

---

## 🐍 How to Regenerate the Data

Clone the repository:


git clone https://github.com/karthic180/retail-analytics-project.git


Install dependencies:


pip install pandas numpy faker


Run:


python python/generate_data.py


This generates fresh retail data for analysis.

---

## 🛠️ Skills Demonstrated

- Dimensional Data Modeling (Star Schema)
- Data Warehousing Concepts
- Advanced DAX & Time Intelligence
- Top N Filtering & Conditional Formatting
- Executive Dashboard Design
- Forecasting & Trend Analysis
- Synthetic Data Engineering
- Git Version Control

---
