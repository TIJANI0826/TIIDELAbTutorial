#Do not change this code
import requests
import unittest
from exercise import balance_check, check_loan_eligibility, calculate_interest, filter_transactions, calculate_total_expense
from send_email import send_message
class ExerciseTest(unittest.TestCase):
##    @classmethod
##    def setUpClass(cls):
##        cls.email = input("Enter the recipient's email: ")
##        cls.first_name = input("Enter the recipient's first name: ")
##        cls.last_name = input("Enter the recipient's last name: ")

    currentResult = None # holds last result object passed to run method

    @classmethod
    def setResult(cls, amount, errors, failures, skipped):
        cls.amount, cls.errors, cls.failures, cls.skipped = \
            amount, errors, failures, skipped

    def tearDown(self):
        amount = self.currentResult.testsRun
        errors = self.currentResult.errors
        failures = self.currentResult.failures
        skipped = self.currentResult.skipped
        self.setResult(amount, errors, failures, skipped)

    @classmethod
    def tearDownClass(cls):
        with open('test.txt', 'w') as file:
            file.write("\ntests run: " + str(cls.amount) + "\n")
            file.write("errors: " + str(len(cls.errors))  + "\n")
            file.write("failures: " + str(len(cls.failures))  + "\n")
            file.write("success: " + str(cls.amount - len(cls.errors) - len(cls.failures))  + "\n")
            file.write("skipped: " + str(len(cls.skipped))  + "\n")
        return cls.amount - len(cls.errors) - len(cls.failures)

    def run(self, result=None):
        self.currentResult = result # remember result for use in tearDown
        unittest.TestCase.run(self, result) # call superclass run method

    def test_balance_check(self):
        # Test cases
        actual1 = balance_check(1000, 500)
        actual2 = balance_check(1000, 1500)
        actual3 = balance_check(500, 500)
        expected1 = (500, "Withdrawal successful!")
        expected2 = (1000, "Insufficient funds.")
        expected3 = (0, "Withdrawal successful!")
        self.assertEqual(actual1, expected1, msg='Expected (500, "Withdrawal successful!")')
        self.assertEqual(actual2, expected2, msg='Expected (1000, "Insufficient funds.")')
        self.assertEqual(actual3, expected3, msg='Expected (0, "Withdrawal successful!")')

    def test_interest_calculation(self):
        # Test cases
        actual1 = calculate_interest(1000, 5, 1)
        actual2 = calculate_interest(2000, 3.5, 2)
        actual3 = calculate_interest(1500, 4, 0.5)
        expected1 = 50
        expected2 = 140
        expected3 = 30
        self.assertEqual(actual1, expected1, msg='Expected 50')
        self.assertEqual(actual2, expected2, msg='Expected 140')
        self.assertEqual(actual3, expected3, msg='Expected 30')

    def test_loan_eligibility(self):
        # Test cases
        actual1 = check_loan_eligibility(25, 35000, 720)
        actual2 = check_loan_eligibility(20, 40000, 750)
        actual3 = check_loan_eligibility(30, 25000, 710)
        actual4 = check_loan_eligibility(40, 45000, 680)
        expected1 = "Eligible for a loan."
        expected2 = "Not eligible for a loan."
        expected3 = "Not eligible for a loan."
        expected4 = "Not eligible for a loan."
        self.assertEqual(actual1, expected1, msg='Expected "Eligible for a loan."')
        self.assertEqual(actual2, expected2, msg='Expected "Not eligible for a loan."')
        self.assertEqual(actual3, expected3, msg='Expected "Not eligible for a loan."')
        self.assertEqual(actual4, expected4, msg='Expected "Not eligible for a loan."')

    def test_transaction_history_filter(self):
        # Test cases
        actual1 = filter_transactions([250.0, 500.0, 75.0, 1000.0, 150.0], 200)
        actual2 = filter_transactions([100.0, 200.0, 300.0], 250)
        actual3 = filter_transactions([50.0, 60.0, 70.0], 100)
        expected1 = [250.0, 500.0, 1000.0]
        expected2 = [300.0]
        expected3 = []
        self.assertEqual(actual1, expected1, msg='Expected [250.0, 500.0, 1000.0]')
        self.assertEqual(actual2, expected2, msg='Expected [300.0]')
        self.assertEqual(actual3, expected3, msg='Expected []')

    def test_monthly_expense_categorization(self):
        # Test cases
        actual1 = calculate_total_expense(1000, 300, 150, 200)
        actual2 = calculate_total_expense(800, 250, 100, 150)
        actual3 = calculate_total_expense(1200, 400, 200, 300)
        expected1 = 1650
        expected2 = 1300
        expected3 = 2100
        self.assertEqual(actual1, expected1, msg='Expected 1650')
        self.assertEqual(actual2, expected2, msg='Expected 1300')
        self.assertEqual(actual3, expected3, msg='Expected 2100')
##    @classmethod
##    def tearDownClass(cls):
##        if not hasattr(cls, 'failureReason'):  # Check if any tests failed
##            send_message(ExerciseTest.email, ExerciseTest.first_name, ExerciseTest.last_name, message="You passed all test for TIIDELAB Pre-Fellowship Python Class Assignment 2 on Control Structures and Functions")

if __name__ == '__main__':
    unittest.main() 

