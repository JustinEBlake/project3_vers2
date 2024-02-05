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

def query(table1, table1cols, table2, table2cols,where_clause=bool, where =str):
    if where_clause == False:
        columns = [[table1+'.'+str(col) for col in table1cols], [table2+'.'+str(col) for col in table2cols]]
        columns_str = ', '.join([','.join(col) for col in columns])
        query = f"SELECT {columns_str} FROM {table1} INNER JOIN {table2} ON {table2}.company_symbol = {table1}.company_symbol"
        return query
    else:
        columns = [[table1+'.'+str(col) for col in table1cols], [table2+'.'+str(col) for col in table2cols]]
        columns_str = ', '.join([','.join(col) for col in columns])
        query = f"SELECT {columns_str} FROM {table1} INNER JOIN {table2} ON {table2}.company_symbol = {table1}.company_symbol WHERE {where}"
        return query




# ------------------------------- Streamlit app -----------------------------------

st.header("Join Tables")
st.divider()

# Allows Users to choose Tables and Columns from Tables
table_1 = st.selectbox(options=tables, label="Choose Table 1")
table_1_cols = st.multiselect(options=get_columns(table_1), label="Choose Columns from Table 1")

st.divider()

table_2 = st.selectbox(options=tables, label="Choose Table 2")
table_2_cols = st.multiselect(options=get_columns(table_2), label="Choose Columns from Table 2")

st.divider()

# Boolen to check if user wants to add a Where Clause in query
where_clause = st.toggle(label="Are there any conditions?")

# Allows user to input specific Where Clause
where = st.text_input(label=" Add condition below. (e.g. Financial_Statements.total_revenue > 8000000 / {table name}.{column name} = {condition})")



join = st.button("Join Tables", key="join_button")
# Button to execute
if join:
    try:
        joined_df = execute_query(query(table_1, table_1_cols, table_2, table_2_cols, where_clause, where))
        st.write("Preview:")
        st.write(joined_df)
        st.divider()

    except Exception as e:
        st.error(f"Error joining tables: {e}")


