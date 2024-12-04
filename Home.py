# streamlit run Home.py
import streamlit as st

# Title and Introduction
st.title("Home")
# st.image("https://source.unsplash.com/800x400/?analytics,charts", caption="Welcome to the Interactive Charts App", use_column_width=True)

st.write("""
Welcome to the **Interactive Charts App**!  
This application allows you to explore and visualize data through various interactive charts.  
Navigate through the pages using the sidebar to access different visualizations and insights.
""")

# Features Section
st.markdown("## Features")
st.markdown("""
- 📊 **Histogram**: Visualize data distributions.  
- 🌌 **Scatter Plot**: Explore relationships between two variables.  
- 📈 **Line Chart**: Analyze trends over time.  
- 📂 **Dataset Preview**: View and summarize the dataset.  
- 🎨 **Interactive Charts**: Compare Box Plot and Pie Chart side by side.  
""")

# Navigation Call-to-Action
st.markdown("""
### 🔍 Explore Now!
Use the **sidebar** on the left to switch between pages and interact with different types of charts.  
Dive into the dataset, analyze trends, and gain insights with ease.
""")

# Optional Footer Section
st.markdown("---")
st.write("Designed with 💡 and 🚀 using **Streamlit**.")
st.markdown(
    "[Learn more about Streamlit](https://streamlit.io) | "
    "[View this project on GitHub](#) | "
    "[Contact the Developer](mailto:developer@example.com)"
)
