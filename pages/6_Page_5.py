import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    file_path = "dataset.csv"
    df = pd.read_csv(file_path)
    return df

df = load_data()

st.title("Dataset")
st.write("Preview of the dataset:")
st.dataframe(df)
st.write("Dataset Summary:")
st.write(df.describe())
