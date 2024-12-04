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

st.title("Scatter Plot")
x_axis = st.sidebar.selectbox("X-axis", df.select_dtypes(include=['int64', 'float64']).columns)
y_axis = st.sidebar.selectbox("Y-axis", df.select_dtypes(include=['int64', 'float64']).columns)
color_col = st.sidebar.selectbox("Color by", df.select_dtypes(include=['object', 'int64']).columns)

fig = px.scatter(df, x=x_axis, y=y_axis, color=color_col, title=f"Scatter Plot of {x_axis} vs {y_axis}")
st.plotly_chart(fig)
