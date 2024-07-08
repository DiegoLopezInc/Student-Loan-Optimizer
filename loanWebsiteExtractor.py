import requests
from bs4 import BeautifulSoup
import loanClass

## Extracting Information from a Loan Webpage
# This script extracts information from a loan webpage and creates a Loan object with the extracted information.

# TODO: Identify the loan webpage URL and the HTML elements containing the loan information.
# Replace the "TODO" placeholders with the appropriate values.

# Target URL (to be replaced with any loan webpage URL)
# TODO: Replace "TODO" with the URL of the loan webpage
url = "TODO"

# Send GET request and get HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Define a function to extract specific information
# Extract all info from a div with class where all loan info is nested
def extract_loan_info():
  # Find element containing name (All loan info is nested in this div)
  # TODO: Replace "TODO" with the class name of the div containing all loan info
  loan_info_element = soup.find("div", class_="TODO")
  if loan_info_element:
    return loan_info_element.text.strip()
  else:
    return None

# Extract information using defined functions
# TODO: Extract specific information based on the loan webpage structure
# TODO: Allow for extraction of multiple loans if needed
loan_info = extract_loan_info()

# Print extracted information
print(f"Loan Info: {loan_info}")

# Create a new Loan object with extracted information
# TODO: Replace values in initializer with the extracted information
loan = loanClass.Loan(lender="Lender", id="ID", principle=1000, interest_rate=0.05, loan_term=12, monthly_payment=100, total_paid=500, total_interest=50)
