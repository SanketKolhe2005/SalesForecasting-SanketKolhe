# 📈 Sales Forecasting & Demand Intelligence System

## 📌 Project Overview

This project is an end-to-end **Sales Forecasting & Demand Intelligence System** developed using Python, Machine Learning, Time Series Analysis, and Streamlit.

The system analyzes historical Superstore sales data, forecasts future sales using XGBoost, detects anomalies, segments products based on demand patterns, and presents business insights through an interactive dashboard.

---

## 🎯 Objectives

- Analyze historical sales data
- Forecast future sales
- Detect unusual sales patterns
- Segment products by demand behavior
- Support inventory and business decision-making
- Build an interactive Streamlit dashboard

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

---

## 📂 Project Structure

```
SalesForecasting_SanketKolhe/
│
├── analysis.ipynb                  # Complete notebook (Tasks 1–8)
├── app.py                          # Streamlit dashboard
├── train.csv                       # Original Superstore dataset
├── clean_sales.csv                 # Cleaned dataset
├── anomaly.csv                     # Anomaly detection results
├── clusters.csv                    # Product clustering results
├── requirements.txt                # Required Python libraries
├── README.md                       # Project documentation
├── summary.pdf                     # Executive business report
│
├── model/
│   └── xgboost_model.pkl           # Trained XGBoost model
│
├── charts/
│   ├── category_sales.png
│   ├── monthly_sales_trend.png
│   ├── time_series_decomposition.png
│   ├── xgboost_forecast.png
│   ├── category_region_forecast.png
│   ├── anomaly_detection.png
│   ├── elbow_method.png
│   └── product_clusters.png
│
└── .gitignore                      # Optional (recommended)
```

---

## 📊 Project Tasks

### Task 1 – Exploratory Data Analysis (EDA)

- Data Cleaning
- Missing Value Treatment
- Sales Analysis
- Category-wise Analysis
- Region-wise Analysis
- Data Visualization

---

### Task 2 – Time Series Forecasting

Implemented:

- Time Series Decomposition
- Monthly Sales Trend Analysis
- Sales Forecasting

Models Compared:

- SARIMA
- Facebook Prophet
- XGBoost

---

### Task 3 – Machine Learning Forecasting

Developed an XGBoost forecasting model using:

- Lag Features
- Rolling Mean
- Month Feature
- Quarter Feature

Evaluation Metrics:

- MAE
- RMSE
- MAPE

---

### Task 4 – Category & Region Forecasting

Generated forecasts for:

- Furniture
- Technology
- Office Supplies

Regional Forecasting:

- East
- West

---

### Task 5 – Anomaly Detection

Implemented:

- Isolation Forest
- Z-Score Method

Detected unusual sales spikes and drops.

---

### Task 6 – Product Demand Segmentation

Used K-Means Clustering to classify products into demand segments.

Features Used:

- Total Sales
- Average Order Value
- Sales Volatility
- Growth Rate

---

### Task 7 – Streamlit Dashboard

Interactive Dashboard Pages:

- 📊 Sales Overview
- 📈 Forecast Explorer
- 🚨 Anomaly Report
- 📦 Demand Segments

---

### Task 8 – Executive Business Report

Prepared a business report summarizing:

- Key Insights
- Forecast Results
- Anomaly Analysis
- Product Segmentation
- Business Recommendations

---

## 📊 Dashboard Features

- Sales Trends
- Category Analysis
- Forecast Explorer
- Demand Segmentation
- Anomaly Detection
- Interactive Charts
- Business Insights

---

## 📷 Sample Dashboard

Dashboard includes:

- Sales Overview
- Forecast Explorer
- Anomaly Report
- Demand Segments

---

## 📈 Results

- Accurate sales forecasting using XGBoost
- Detection of unusual sales behavior
- Product demand segmentation
- Interactive visualization using Streamlit

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/SalesForecasting-SanketKolhe.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 📁 Dataset

Dataset Used:

**Superstore Sales Dataset**

---

## 👨‍💻 Author

**Sanket Kolhe**

B.Tech Computer Engineering

MIT Academy of Engineering, Alandi, Pune

GitHub: https://github.com/SanketKolhe2005

LinkedIn: https://www.linkedin.com/in/sanket-kolhe-b2683525b

---

## ⭐ Future Enhancements

- Deep Learning Forecasting (LSTM)
- Real-time Dashboard Updates
- Cloud Deployment
- Automated Inventory Alerts
- Sales Recommendation System

---

## 📄 License

This project is developed for educational and internship purposes.
