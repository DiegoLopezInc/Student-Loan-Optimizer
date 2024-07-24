'''
Class to represent a loan. Contains the following attributes:
- lender: The name of the lender
- id: The unique identifier of the loan
- principle: The initial loan amount
- interest_rate: The annual interest rate of the loan
- loan_term: The duration of the loan in months
- monthly_payment: The monthly payment amount
- total_paid: The total amount paid towards the loan
- remainder: The remaining loan amount
- total_interest: The total interest paid on the loan
'''
class Loan:
    def __init__(
        self,
        lender,
        id,
        principle,
        interest_rate,
        loan_term,
        monthly_payment,
        total_paid,
        total_interest,
    ):
        self.lender = lender
        self.id = id
        self.principle = principle
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.monthly_payment = monthly_payment
        self.total_paid = total_paid
        self.remainder = principle - total_paid
        self.total_interest = total_interest

    # String representation of the Loan object
    def __str__(self):
        return f"Lender: {self.lender}, Id: {self.id}, Principle: {self.principle}, Interest Rate: {self.interest_rate}, Loan Term: {self.loan_term}, Monthly Payment: {self.monthly_payment}, Total Paid: {self.total_paid}, Remainder: {self.remainder}, Total Interest: {self.total_interest}"
