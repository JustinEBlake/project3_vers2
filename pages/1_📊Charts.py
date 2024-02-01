import streamlit as st
import pandas as pd
import plotly.express as px
from app import conn

# Create cursor object
cursor = conn.cursor()

# Execute a query to get the list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Get all table names
tables_raw = cursor.fetchall()

# Store tables in list
tables = [table[0] for table in tables_raw]

# Empty columns list to store columns
columns = []

# Loop through tables 
for table in tables:
    # Execute a query to get column names for each table
    cursor.execute(f"PRAGMA table_info({table});")

    # Fetch column name
    column_name_raw = cursor.fetchall()

    for column in column_name_raw:
        column_name = column[1]

        if column_name not in columns:
            columns.append(column_name)


# Streamlit app

st.header("Create Visuals")
st.divider()
table_1 = st.selectbox(options=tables, label="Choose Table")
table_2 = st.selectbox(options=columns, label="Choose Column")



# Button to execute
st.button("Execute Visual")