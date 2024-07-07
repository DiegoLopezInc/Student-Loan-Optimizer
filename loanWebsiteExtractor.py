import requests
from bs4 import BeautifulSoup

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
loan_info = extract_loan_info()

# Print extracted information
print(f"Loan Info: {loan_info}")