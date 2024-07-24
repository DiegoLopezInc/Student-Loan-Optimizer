import unittest
from .test_loanClass import TestLoan
from .test_loan_scraper import TestLoanScraper
from .test_loan_analyzer import TestLoanAnalyzer
from .test_refinance_calculator import TestRefinanceCalculator

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestLoan))
    test_suite.addTest(unittest.makeSuite(TestLoanScraper))
    test_suite.addTest(unittest.makeSuite(TestLoanAnalyzer))
    test_suite.addTest(unittest.makeSuite(TestRefinanceCalculator))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)

if __name__ == '__main__':
    run_tests()
