import streamlit as st
import pandas as pd
import sqlite3

# Connect to SQlit database 
conn = sqlite3.connect('company_data.sqlite')

# Create cursor object
cursor = conn.cursor()

# Execute a query to get the list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Get all table names
tables_raw = cursor.fetchall()

# Store tables in list
tables = [table[0] for table in tables_raw]


def get_columns(table_name):
    # Empty columns list to store columns
    columns = []

    # Execute a query to get column names for table
    cursor.execute(f"PRAGMA table_info({table_name});")

    # Fetch column name
    column_name_raw = cursor.fetchall()

    # Get column name and append to empty columns list
    for column in column_name_raw:
        column_name = column[1]

        if column_name not in columns:
            columns.append(column_name)
    
    return columns


# Function to execute custom SQL query

def execute_query(query):
    result = pd.read_sql_query(query, conn)
    return result

# Function to create query based on user selected boxes
def query(table1, table1cols, table2, table2cols):
    columns = [table1 + "." + table1cols, table2 + "." + table2cols]
    columns_str = ', '.join(columns)
    query = f"SELECT {columns_str} FROM {table1} INNER JOIN {table2} ON {table2}.company_symbol = {table1}.company_symbol"
    return query

def make_chart(file,col1, col2):
    df = pd.read_csv(file)

    x_axis = col1
    y_axis = col2
    chart = st.bar_chart(df,x=x_axis,y=y_axis)

    return chart


# ------------------------------- Streamlit app -----------------------------------

st.header("Make Bar Chart")
# Heads up
st.caption("⚠️ Only creates bar chart after joing two tables.")
st.divider()
table_1 = st.selectbox(options=tables, label="Choose Table 1")
table_1_cols = st.selectbox(options=get_columns(table_1), label="Choose X Axis")

st.divider()

table_2 = st.selectbox(options=tables, label="Choose Table 2")
table_2_cols = st.selectbox(options=get_columns(table_2), label="Choose Y Axis")

st.divider()

chart = st.button("Make Bar Chart")
# Button to execute
if chart:
    try:
        joined_df = execute_query(query(table_1, table_1_cols, table_2, table_2_cols))
        st.write("Preview:")
        st.bar_chart(joined_df, x=table_1_cols, y=table_2_cols)
        st.divider()

        
    except Exception as e:
        st.error(f"Error joining tables: {e}")



