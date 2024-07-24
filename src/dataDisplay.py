import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from loan_scraper import scrape_loan_data
from loan_analyzer import graph_future_payments
from refinance_calculator import calculate_refinance_options

st.title('Student Loan Optimizer')

# Loan Data Display
st.header('Current Loans')
loans = scrape_loan_data('https://example-loan-provider.com/loans')
loan_data = [
    {
        'Lender': loan.lender,
        'ID': loan.id,
        'Principle': loan.principle,
        'Interest Rate': f'{loan.interest_rate:.2%}',
        'Loan Term': loan.loan_term,
        'Monthly Payment': loan.monthly_payment,
        'Total Paid': loan.total_paid,
        'Remainder': loan.remainder,
        'Total Interest': loan.total_interest
    }
    for loan in loans
]
st.table(pd.DataFrame(loan_data))

# Future Payments Graph
st.header('Future Payments Graph')
selected_loan = st.selectbox('Select a loan to graph', options=[loan.id for loan in loans])
selected_loan_obj = next(loan for loan in loans if loan.id == selected_loan)
months = st.slider('Number of months to project', min_value=12, max_value=360, value=120, step=12)

graph_future_payments(selected_loan_obj, months)
st.image(f'loan_{selected_loan}_payments.png')

# Refinancing Options
st.header('Refinancing Options')
new_rates = [0.03, 0.035, 0.04, 0.045, 0.05]
new_terms = [120, 180, 240, 360]
refinance_options = calculate_refinance_options(selected_loan_obj, new_rates, new_terms)

options_data = [
    {
        'Interest Rate': f'{option["interest_rate"]:.2%}',
        'Term (months)': option['term'],
        'Monthly Payment': f'${option["monthly_payment"]:.2f}',
        'Total Interest': f'${option["total_interest"]:.2f}'
    }
    for option in refinance_options
]
st.table(pd.DataFrame(options_data))