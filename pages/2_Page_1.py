import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data
def load_data():
    file_path = "dataset.csv"  # Adjust as needed
    df = pd.read_csv(file_path)
    return df

df = load_data()

st.title("Histogram")
x_axis = st.sidebar.selectbox("X-axis", df.select_dtypes(include=['int64', 'float64']).columns)
bins = st.sidebar.slider("Number of bins", 5, 50, 10)

fig, ax = plt.subplots()
ax.hist(df[x_axis].dropna(), bins=bins, color="skyblue", edgecolor="black")
ax.set_title(f"Histogram of {x_axis}")
ax.set_xlabel(x_axis)
ax.set_ylabel("Frequency")
st.pyplot(fig)
