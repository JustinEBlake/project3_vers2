import streamlit as st
import pandas as pd
import sqlite3

# Connect to SQlit database 
conn = sqlite3.connect('company_data.sqlite')

# Function to execute custom SQL query
def execute_query(query):
    result = pd.read_sql_query(query, conn)
    return result

# Streamlit app with query input
st.title("Financial Database Query")

# Divider
st.divider()

# User input for SQL query
query_input = st.text_area("Enter your SQL query:")

# Execute query button
if st.button("Execute Query"):
    try:
        result_df = execute_query(query_input)
        st.write("Query Result:")
        st.write(result_df)
    except Exception as e:
        st.error(f"Error executing query: {e}")