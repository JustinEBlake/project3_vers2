import streamlit as st
import sqlite3
import pandas as pd

# Connect to SQlit database 
conn = sqlite3.connect('company_data.sqlite')

# Function to read data from tables
def load_data():
    companies = pd.read_sql_query("SELECT * FROM Companies", conn)
    financial_statements = pd.read_sql_query("SELECT * FROM Financial_Statements", conn)
    balance_sheets = pd.read_sql_query("SELECT * FROM Balance_Sheets", conn)
    stocks = pd.read_sql_query("SELECT * FROM Stocks", conn)
    return companies, financial_statements, balance_sheets, stocks

# Load data
companies, financial_statements, balance_sheets, stocks = load_data()

# Streamlit app

# Layout config
col1, col2 = st.columns([1,2])

# Header
st.title("Financial Database Visualization App")

# Display tables
st.header("Companies")
st.write(companies)

st.header("Financial Statements")
st.write(financial_statements)

st.header("Balance Sheets")
st.write(balance_sheets)

st.header("Stocks")
st.write(stocks)

