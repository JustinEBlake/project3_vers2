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
    columns = [[table1+'.'+str(col) for col in table1cols], [table2+'.'+str(col) for col in table2cols]]
    columns_str = ', '.join([','.join(col) for col in columns])
    query = f"SELECT {columns_str} FROM {table1} INNER JOIN {table2} ON {table2}.company_symbol = {table1}.company_symbol"
    return query

# ------------------------------- Streamlit app -----------------------------------

st.header("Create Visuals")
st.divider()
table_1 = st.selectbox(options=tables, label="Choose Table 1")
table_1_cols = st.multiselect(options=get_columns(table_1), label="Choose Columns from Table 1")
table_2 = st.selectbox(options=tables, label="Choose Table 2")
table_2_cols = st.multiselect(options=get_columns(table_2), label="Choose Columns from Table 2")


# Button to execute
if st.button("Join Tables"):
    try:
        joined_df = execute_query(query(table_1, table_1_cols, table_2, table_2_cols))
        st.write("Preview:")
        st.write(joined_df)
    except Exception as e:
        st.error(f"Error joining tables: {e}")

st.divider()