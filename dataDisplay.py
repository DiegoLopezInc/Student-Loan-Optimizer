import streamlit as st
import pandas as pd
import numpy as np

"""
# Loan Data Display
Using loan data to create a table:
"""

st.title('Loan Data Display')

st.write("Here's my first attempt at using data to create a table:")

# TODO: Replace the below code with the extracted loan data
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


