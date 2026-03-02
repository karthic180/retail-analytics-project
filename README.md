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

---

## 🏗️ Data Model

The solution uses a **Star Schema** design:

### Fact Table
- fact_sales

### Dimension Tables
- dim_customer
- dim_product
- dim_date

**Grain:** One row per product per transaction per day.

---

## 📊 Dashboard Pages

### 1️⃣ Executive Overview

<img src="https://raw.githubusercontent.com/karthic180/retail-analytics-project/main/screenshots/page%201.jpg" width="800">

---

### 2️⃣ Product Insights

<img src="https://raw.githubusercontent.com/karthic180/retail-analytics-project/main/screenshots/page%202.jpg" width="800">

---

### 3️⃣ Customer Analytics

<img src="https://raw.githubusercontent.com/karthic180/retail-analytics-project/main/screenshots/page%203.jpg" width="800">

---

## 📄 Full Power BI Report (PDF)

You can download the full exported Power BI report here:

👉 [Download Report](https://github.com/karthic180/retail-analytics-project/blob/main/reports/retail-analytics-project.pdf)

---

## 🐍 How to Regenerate the Data

Clone the repository:


git clone https://github.com/karthic180/retail-analytics-project.git


Install dependencies:


pip install pandas numpy faker


Run:


python python/generate_data.py


---

## 🛠️ Skills Demonstrated

- Star Schema & Dimensional Modeling
- Advanced DAX & Time Intelligence
- Forecasting in Power BI
- Top N Analysis
- Data-Driven Decision Making
- Python Data Generation
- Git Version Control

---
