import streamlit as st
import pandas as pd



def make_chart(file,col1, col2):
    df = pd.read_csv(file)

    x_axis = col1
    y_axis = col2
    chart = st.bar_chart(df,x=x_axis,y=y_axis)

    return chart

# Write Header
st.header("Make A Bar Chart")
st.divider()

file = st.file_uploader("Upload CSV Here")

x_axis = st.text_input("Input column for X Axis")
y_axis = st.text_input("Input column for Y Axis")


if st.button("Click to Chart Uploaded Data"):
    make_chart(file,x_axis, y_axis)