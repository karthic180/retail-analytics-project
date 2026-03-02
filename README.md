\# Retail Sales Analytics \& Forecasting Project



\## 📊 Project Overview



This project is an end-to-end Business Intelligence solution built using:



\- Python (Synthetic Data Generation)

\- Dimensional Data Modeling (Star Schema)

\- Power BI (Interactive Dashboard \& Forecasting)

\- DAX (Advanced Measures \& Time Intelligence)



The goal is to simulate a real-world retail analytics environment and demonstrate data modeling, reporting, and predictive analysis skills.



---



\## 🏗️ Data Architecture



The project follows a \*\*Star Schema\*\* design:



\### Fact Table

\- fact\_sales



\### Dimension Tables

\- dim\_customer

\- dim\_product

\- dim\_date



\### Grain

One row per product sold per transaction per day.



This structure enables efficient analytics and scalable reporting.



---



\## 🐍 Synthetic Data Generation



Retail data is generated using Python.



To regenerate the dataset:



```bash

python python/generate\_data.py



