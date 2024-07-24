import unittest
from src.loanClass import Loan

class TestLoan(unittest.TestCase):
    def setUp(self):
        self.loan = Loan("TestLender", "ID123", 10000, 0.05, 120, 100, 1000, 500)

    def test_loan_initialization(self):
        self.assertEqual(self.loan.lender, "TestLender")
        self.assertEqual(self.loan.id, "ID123")
        self.assertEqual(self.loan.principle, 10000)
        self.assertEqual(self.loan.interest_rate, 0.05)
        self.assertEqual(self.loan.loan_term, 120)
        self.assertEqual(self.loan.monthly_payment, 100)
        self.assertEqual(self.loan.total_paid, 1000)
        self.assertEqual(self.loan.remainder, 9000)
        self.assertEqual(self.loan.total_interest, 500)

    def test_loan_str_representation(self):
        expected_str = "Lender: TestLender, Id: ID123, Principle: 10000, Interest Rate: 0.05, Loan Term: 120, Monthly Payment: 100, Total Paid: 1000, Remainder: 9000, Total Interest: 500"
        self.assertEqual(str(self.loan), expected_str)

if __name__ == '__main__':
    unittest.main()