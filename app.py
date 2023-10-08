import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import os
import warnings
warnings.filterwarnings('ignore')
  
# Load data from a CSV file (replace with your data path)
csv_file_path = r"C:\Users\hp.MUKESH-LF4B6N6\Desktop\NewAirbnb.csv"
df = pd.read_csv(csv_file_path)

# Set a title for your Streamlit app
st.title("Airbnb Data visulization")

# Create a scatter plot
st.header(" Airbnb dataset")

# Choose the chart type
chart_type = st.sidebar.radio(  "___*Select Chart Type* ___", ["Area Chart","Line chart","Bar Chart", "Histogram", "Scatter Plots"])

# Filter numeric columns for the heatmap
numeric_columns = df.select_dtypes(include=['float64', 'int64'])


st.set_option('deprecation.showPyplotGlobalUse', False)

# Allow the user to select the X and Y axes columns from the dataset
x_axis_column = st.selectbox("Select X-axis Column", df.columns)
y_axis_column = st.selectbox("Select Y-axis Column", df.columns)

if  st.sidebar.button("Generate Area Chart"):
    plt.figure(figsize=(10, 6))
    plt.fill_between(df[x_axis_column], df[y_axis_column], alpha=0.5)
    plt.xlabel(x_axis_column)
    plt.ylabel(y_axis_column)
    plt.title(f"Area Chart of {y_axis_column} Over {x_axis_column}")
    st.pyplot()


elif st.sidebar.button("Generate Line Chart"):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df[x_axis_column], df[y_axis_column])
    ax.set_xlabel(x_axis_column)
    ax.set_ylabel(y_axis_column)
    ax.set_title(f"Line Chart of {y_axis_column} over {x_axis_column}")
    st.pyplot(fig)

elif st.sidebar.button("Generate Bar Chart"):
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_axis_column], df[y_axis_column])
    plt.xlabel(x_axis_column)
    plt.ylabel(y_axis_column)
    plt.title(f"{y_axis_column} Over {x_axis_column}")
    st.pyplot()

elif st.sidebar.button("Generate Histogram "):
    fig = px.histogram(df[x_axis_column], df[y_axis_column])
    st.plotly_chart(fig)

elif st.sidebar.button("Scatter Plots"):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df[x_axis_column], df[y_axis_column])
    ax.set_xlabel(x_axis_column)
    ax.set_ylabel(y_axis_column)
    ax.set_title(f"Scatter Plot of {y_axis_column} vs {x_axis_column}")
    st.pyplot(fig)
