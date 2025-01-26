import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize the Streamlit app
st.set_page_config(page_title="Personal Finance Dashboard", layout="wide", initial_sidebar_state="expanded")
st.title("Personal Finance Dashboard")

# Placeholder account balances
data_accounts = [
    {"Account Name": "USAA Checking", "Balance": 4500.13, "Currency": "USD"},
    {"Account Name": "AMEX Savings", "Balance": 20348.05, "Currency": "USD"},
    {"Account Name": "Local Bank", "Balance": 500.50, "Currency": "EUR"},
    {"Account Name": "Wise", "Balance": 1200.75, "Currency": "EUR"}
]

data_expenses = {
    "Category": ["Groceries", "Rent", "Entertainment", "Utilities", "Transportation"],
    "Amount": [600, 1500, 300, 200, 150]
}

data_budget = {
    "Category": ["Groceries", "Rent", "Utilities", "Transportation", "Savings"],
    "Budget": [500, 1500, 250, 200, 300],
    "Actual": [600, 1500, 200, 180, 400]
}

credit_card_data = [
    {"Credit Card": "USAA", "Balance": 3774.12, "Credit Limit": 5000},
    {"Credit Card": "AMEX", "Balance": 1645.98, "Credit Limit": 3000}
]

savings_data = [
    {"Year": 2025, "Monthly Savings": 300},
    {"Year": 2026, "Monthly Savings": 400},
    {"Year": 2027, "Monthly Savings": 500},
    {"Year": 2028, "Monthly Savings": 600},
    {"Year": 2029, "Monthly Savings": 700}
]

investment_growth = [10000, 12000, 14000, 16500, 19000]

def account_balance_section():
    st.subheader("All Account Balances")
    df_accounts = pd.DataFrame(data_accounts)
    df_accounts["Converted Balance (USD)"] = df_accounts["Converted Balance (USD)"] = df_accounts.apply(lambda row: round(row["Balance"] * 1.1, 2) if row["Currency"] == "EUR" else row["Balance"], axis=1)
    st.table(df_accounts)
    st.metric("Total Balance (USD)", f"${df_accounts['Converted Balance (USD)'].sum():,.2f}")

def spending_by_category():
    st.subheader("Spending by Category")
    df_expenses = pd.DataFrame(data_expenses)
    fig, ax = plt.subplots()
    sns.barplot(x="Amount", y="Category", data=df_expenses, palette="Blues", ax=ax)
    ax.set_title("Spending by Category")
    st.pyplot(fig, clear_figure=True)

def household_budget_section():
    st.subheader("Household Budget Analysis")
    df_budget = pd.DataFrame(data_budget)
    fig, ax = plt.subplots()
    bar_width = 0.35
    index = np.arange(len(df_budget))

    ax.bar(index - bar_width/2, df_budget['Budget'], bar_width, label="Budget", color="green")
    ax.bar(index + bar_width/2, df_budget['Actual'], bar_width, label="Actual", color="blue")
    ax.set_title("Budget vs Actual")
    ax.set_xticks(index)
    ax.set_xticklabels(df_budget['Category'])
    ax.legend()
    st.pyplot(fig)

def credit_building_insights():
    st.subheader("Credit Building Insights")
    df_credit = pd.DataFrame(credit_card_data)
    df_credit['Utilization (%)'] = (df_credit['Balance'] / df_credit['Credit Limit']) * 100
    st.dataframe(df_credit, use_container_width=True)

    for _, row in df_credit.iterrows():
        utilization = row['Utilization (%)']
        if utilization > 30:
            st.warning(f"{row['Credit Card']}: Utilization is {utilization:.2f}%. Aim to reduce it below 30% to improve your credit score.")
        else:
            st.success(f"{row['Credit Card']}: Utilization is {utilization:.2f}%. Excellent credit management!")

def savings_projection():
    st.subheader("Savings Insights")
    df_savings = pd.DataFrame(savings_data)
    fig, ax = plt.subplots()
    ax.plot(df_savings['Year'], df_savings['Monthly Savings'], marker="o")
    ax.set_title("Savings Growth Over Time")
    ax.set_ylabel("Monthly Savings (USD)")
    ax.set_xlabel("Year")
    st.pyplot(fig)

def investment_insights():
    st.subheader("Passive Investment Insights")
    years = [1, 2, 3, 4, 5]
    fig, ax = plt.subplots()
    ax.plot(years, investment_growth, marker="o", color="gold")
    ax.set_title("Investment Growth Over Time")
    ax.set_ylabel("Portfolio Value (USD)")
    ax.set_xlabel("Year")
    st.pyplot(fig)

# Render sections
account_balance_section()
spending_by_category()
household_budget_section()
credit_building_insights()
savings_projection()
investment_insights()
