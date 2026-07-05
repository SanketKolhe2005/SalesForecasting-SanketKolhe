# ===========================
# Import Libraries
# ===========================

import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# ===========================
# Page Configuration
# ===========================

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Sales Forecasting & Demand Intelligence System")

# ===========================
# Load Dataset
# ===========================

@st.cache_data
def load_data():
    df = pd.read_csv("clean_sales.csv")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

df = load_data()

# ===========================
# Load Model
# ===========================

@st.cache_resource
def load_model():
    return joblib.load("model/xgboost_model.pkl")

model = load_model()

# ===========================
# Sidebar
# ===========================

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Sales Overview",
        "Forecast Explorer",
        "Anomaly Report",
        "Demand Segments"
    ]
)

# ===========================
# PAGE 1
# ===========================

if page == "Sales Overview":

    st.header("Sales Overview")

    yearly = df.groupby("Year")["Sales"].sum().reset_index()

    fig = px.bar(
        yearly,
        x="Year",
        y="Sales",
        title="Total Sales by Year"
    )

    st.plotly_chart(fig, use_container_width=True)

    monthly = (
        df.groupby("Order Date")["Sales"]
        .sum()
        .resample("ME")
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly,
        x="Order Date",
        y="Sales",
        title="Monthly Sales Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

# ===========================
# PAGE 2
# ===========================

elif page == "Forecast Explorer":

    st.header("Forecast Explorer")

    category = st.selectbox(
        "Select Category",
        df["Category"].unique()
    )

    horizon = st.slider(
        "Forecast Horizon",
        1,
        3,
        3
    )

    sales = df[df["Category"] == category]

    monthly = (
        sales.groupby("Order Date")["Sales"]
        .sum()
        .resample("ME")
        .sum()
    )

    st.subheader("Historical Monthly Sales")
    st.line_chart(monthly)

    # Placeholder forecast (replace with your XGBoost prediction later)
    forecast = monthly.tail(horizon).values

    forecast_df = pd.DataFrame({
        "Month": [f"Month {i+1}" for i in range(horizon)],
        "Forecast Sales": forecast
    })

    st.subheader("Forecast")
    st.dataframe(forecast_df)

# ===========================
# PAGE 3
# ===========================

elif page == "Anomaly Report":

    st.header("Anomaly Report")

    anomaly = pd.read_csv("anomaly.csv")

    st.dataframe(anomaly)

    if "Sales" in anomaly.columns:

        fig = px.line(
            anomaly,
            y="Sales",
            title="Weekly Sales"
        )

        st.plotly_chart(fig, use_container_width=True)

# ===========================
# PAGE 4
# ===========================

elif page == "Demand Segments":

    st.header("Demand Segments")

    cluster = pd.read_csv("clusters.csv")

    st.dataframe(cluster)

    if (
        "PCA1" in cluster.columns
        and "PCA2" in cluster.columns
        and "Demand_Segment" in cluster.columns
    ):

        fig = px.scatter(
            cluster,
            x="PCA1",
            y="PCA2",
            color="Demand_Segment",
            hover_name="Sub-Category"
        )

        st.plotly_chart(fig, use_container_width=True)