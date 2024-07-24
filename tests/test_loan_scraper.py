import unittest
from unittest.mock import patch, MagicMock
from src.loan_scraper import scrape_loan_data
from src.loanClass import Loan

class TestLoanScraper(unittest.TestCase):
    @patch('src.loan_scraper.requests.get')
    def test_scrape_loan_data(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = '''
        <div class="loan-item">
            <span class="lender">TestLender</span>
            <span class="id">ID123</span>
            <span class="principle">10000</span>
            <span class="interest-rate">0.05</span>
            <span class="loan-term">120</span>
            <span class="monthly-payment">100</span>
            <span class="total-paid">1000</span>
            <span class="total-interest">500</span>
        </div>
        '''
        mock_get.return_value = mock_response

        loans = scrape_loan_data('https://example.com')

        self.assertEqual(len(loans), 1)
        loan = loans[0]
        self.assertIsInstance(loan, Loan)
        self.assertEqual(loan.lender, "TestLender")
        self.assertEqual(loan.id, "ID123")
        self.assertEqual(loan.principle, 10000)
        self.assertEqual(loan.interest_rate, 0.05)
        self.assertEqual(loan.loan_term, 120)
        self.assertEqual(loan.monthly_payment, 100)
        self.assertEqual(loan.total_paid, 1000)
        self.assertEqual(loan.total_interest, 500)

if __name__ == '__main__':
    unittest.main()