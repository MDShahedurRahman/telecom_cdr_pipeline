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
