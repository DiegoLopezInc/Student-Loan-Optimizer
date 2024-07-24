import unittest
from unittest.mock import patch, MagicMock
from src.loan_analyzer import calculate_future_payments, graph_future_payments
from src.loanClass import Loan

class TestLoanAnalyzer(unittest.TestCase):
    def setUp(self):
        self.loan = Loan("TestLender", "ID123", 10000, 0.05, 120, 100, 1000, 500)

    def test_calculate_future_payments(self):
        payments = calculate_future_payments(self.loan, 12)
        self.assertEqual(len(payments), 12)
        self.assertAlmostEqual(payments[0], 100, places=2)

    @patch('src.loan_analyzer.plt')
    def test_graph_future_payments(self, mock_plt):
        graph_future_payments(self.loan, 12)
        mock_plt.figure.assert_called_once()
        mock_plt.plot.assert_called_once()
        mock_plt.title.assert_called_once()
        mock_plt.xlabel.assert_called_once()
        mock_plt.ylabel.assert_called_once()
        mock_plt.grid.assert_called_once()
        mock_plt.savefig.assert_called_once()
        mock_plt.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()