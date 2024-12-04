import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    file_path = "dataset.csv"
    df = pd.read_csv(file_path)
    return df

df = load_data()

st.title("Interactive Charts")

# Tabs for Box Plot and Pie Chart
tab1, tab2 = st.tabs(["Box Plot", "Pie Chart"])

# Tab 1: Box Plot
with tab1:
    st.subheader("Box Plot")
    x_axis = st.selectbox("Categorical Variable (X-axis)", df.select_dtypes(include=['object']).columns, key="box_x")
    y_axis = st.selectbox("Numerical Variable (Y-axis)", df.select_dtypes(include=['int64', 'float64']).columns, key="box_y")
    
    fig_box = px.box(df, x=x_axis, y=y_axis, title=f"Box Plot of {y_axis} by {x_axis}")
    st.plotly_chart(fig_box, use_container_width=True)

# Tab 2: Pie Chart
with tab2:
    st.subheader("Pie Chart")
    category = st.selectbox("Categorical Variable", df.select_dtypes(include=['object']).columns, key="pie_category")
    
    fig_pie = px.pie(df, names=category, title=f"Distribution of {category}")
    st.plotly_chart(fig_pie, use_container_width=True)
