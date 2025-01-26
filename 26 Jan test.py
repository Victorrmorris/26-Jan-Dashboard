import streamlit as st
import pandas as pd

# Initialize the Streamlit app
st.set_page_config(page_title="Personal Finance Dashboard", layout="wide")
st.title("Personal Finance Dashboard")

# Placeholder data
accounts = [
    {"Account": "USAA Checking", "Balance": 4500.13},
    {"Account": "AMEX Savings", "Balance": 20348.05},
    {"Account": "Local Bank", "Balance": 500.50},
    {"Account": "Wise", "Balance": 1200.75}
]

expenses = [
    {"Category": "Groceries", "Amount": 600},
    {"Category": "Rent", "Amount": 1500},
    {"Category": "Entertainment", "Amount": 300},
    {"Category": "Utilities", "Amount": 200},
    {"Category": "Transportation", "Amount": 150}
]

# Display Account Balances
st.subheader("Account Balances")
df_accounts = pd.DataFrame(accounts)
st.table(df_accounts)

# Display Spending by Category
st.subheader("Spending by Category")
df_expenses = pd.DataFrame(expenses)
st.bar_chart(df_expenses.set_index("Category"))

# Placeholder for Budget Insights
st.subheader("Budget Insights")
st.write("Coming soon: Detailed budget analysis and recommendations!")
