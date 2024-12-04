import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    file_path = "dataset.csv"
    df = pd.read_csv(file_path)
    df['ADMISSION DATE'] = pd.to_datetime(df['ADMISSION DATE'], errors='coerce')
    return df

df = load_data()

st.title("Line Chart")
x_axis = st.sidebar.selectbox("X-axis (time or numerical)", df.select_dtypes(include=['datetime64', 'int64', 'float64']).columns)
y_axis = st.sidebar.selectbox("Y-axis", df.select_dtypes(include=['int64', 'float64']).columns)

fig = px.line(df, x=x_axis, y=y_axis, title=f"Line Chart of {x_axis} vs {y_axis}")
st.plotly_chart(fig)
