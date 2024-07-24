import unittest
from src.refinance_calculator import calculate_refinance_options
from src.loanClass import Loan

class TestRefinanceCalculator(unittest.TestCase):
    def setUp(self):
        self.loan = Loan("TestLender", "ID123", 10000, 0.05, 120, 100, 1000, 500)

    def test_calculate_refinance_options(self):
        new_rates = [0.03, 0.04]
        new_terms = [120, 180]
        options = calculate_refinance_options(self.loan, new_rates, new_terms)

        self.assertEqual(len(options), 4)
        for option in options:
            self.assertIn('interest_rate', option)
            self.assertIn('term', option)
            self.assertIn('monthly_payment', option)
            self.assertIn('total_interest', option)

        self.assertEqual(options[0]['interest_rate'], 0.03)
        self.assertEqual(options[0]['term'], 120)
        self.assertGreater(options[0]['monthly_payment'], 0)
        self.assertGreater(options[0]['total_interest'], 0)

if __name__ == '__main__':
    unittest.main()