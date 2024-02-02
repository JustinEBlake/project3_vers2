import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def make_chart(file,x_axis, y_axis):
    df = pd.DataFrame(file)

    chart = st.bar_chart(df,x=x_axis,y=y_axis)

    return chart

# Write Header
st.header("Make A Bar Chart")
st.divider()

file = st.file_uploader("Upload CSV Here")

x_axis = st.text_input("Input column for X Axis")
y_axis = st.text_input("Input column for Y Axis")


st.button("Click to Chart Uploaded Data", on_click=make_chart(file, x_axis, y_axis))