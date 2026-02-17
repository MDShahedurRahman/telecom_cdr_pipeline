# Telecom Call Data Engineering Pipeline (PySpark)

A complete **Telecom Call Detail Records (CDR) Data Engineering Pipeline** built using **PySpark** and the modern **Medallion Architecture (Bronze → Silver → Gold)**.

This project processes raw telecom call transaction data from CSV, cleans and transforms it into Parquet format, applies anomaly detection rules, builds a Star Schema model, and generates business KPIs for telecom analytics.

It is designed as a **portfolio-quality Data Engineering project** demonstrating real-world ETL workflows, scalable lakehouse design, and analytics-ready outputs.

---

## 🚀 Project Overview

Telecom companies generate billions of call records daily.  
These records are used for:

- Revenue reporting  
- Customer usage analytics  
- Fraud and anomaly detection  
- Operational monitoring  

Raw call transaction data must be transformed into structured, analytics-ready datasets.

This pipeline performs:

- Raw data ingestion into a Data Lake (Bronze)
- Data cleaning and standardization (Silver)
- Call anomaly detection (Long calls, International calls)
- Star Schema modeling for analytics (Gold)
- Business KPI queries for insights

---

## 🏗 Pipeline Architecture (Medallion Design)

```
Raw CSV Call Records
        ↓
Bronze Layer (Raw Parquet)
        ↓
Silver Layer (Cleaned + Standardized Parquet)
        ↓
Anomaly Detection Layer (Flagged Calls)
        ↓
Gold Layer (Star Schema Tables)
        ↓
Business Queries + Telecom KPI Reports
```

---

## 📂 Project Structure

```
telecom_cdr_pipeline/
│
├── main.py
├── config.py
├── requirements.txt
│
├── data/
│   └── call_records.csv
│
├── jobs/
│   ├── bronze_ingestion.py
│   ├── silver_cleaning.py
│   ├── anomaly_detection.py
│   ├── gold_star_schema.py
│   └── business_queries.py
│
├── utils/
│   ├── spark_session.py
│   ├── schema_definitions.py
│   └── helpers.py
│
└── output/
    ├── bronze/
    ├── silver/
    ├── gold/
    └── reports/
```

---

## 📌 Data Source

The pipeline uses a sample telecom dataset:

`data/call_records.csv`

Example:

```csv
call_id,customer_id,customer_name,call_type,duration_minutes,call_cost,call_date,city,country
1,C001,John Smith,Local,15,5,2025-01-05,New York,USA
2,C002,Amina Rahman,International,45,25,2025-01-06,Boston,USA
3,C003,Sarah Lee,Local,200,60,2025-01-08,Chicago,USA
```

---


## ⚙️ Technologies Used

- **Python**
- **PySpark**
- **Parquet Storage Format**
- **Medallion Data Lake Architecture**
- **Anomaly Detection Engineering**
- **Star Schema Data Modeling**
- **Telecom KPI Analytics Queries**

---

## 🚀 Pipeline Jobs

---

### 🥉 Bronze Layer: Raw Data Ingestion

**File:** `jobs/bronze_ingestion.py`

Responsibilities:

- Read raw call transaction CSV data
- Apply schema validation
- Store raw records in Parquet format

Output:

```
output/bronze/
```

---

### 🥈 Silver Layer: Data Cleaning & Transformation

**File:** `jobs/silver_cleaning.py`

Transformations applied:

- Remove duplicate call records
- Handle missing values
- Convert call_date into proper DateType

Output:

```
output/silver/
```

---
