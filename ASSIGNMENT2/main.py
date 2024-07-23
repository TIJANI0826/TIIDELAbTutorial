import exercise
from unittest import main, TextTestRunner
from test_module import ExerciseTest
import io
import sys
from send_email import send_message

# Do not change the function below
def extract_success_number(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if 'success' in line:
                # Extract the number after "success:"
                parts = line.split('success:')
                if len(parts) > 1:
                    number_str = parts[1].strip().split()[0]
                    try:
                        number = int(number_str)
                        return number
                    except ValueError:
                        return None
    return None

#You can change the code below to test your function
# Test your function by calling it here 
# exercise.balance_check(1000, 500)
# exercise.calculate_interest(1000, 5, 1)
# exercise.check_loan_eligibility(25, 35000, 720)
# exercise.calculate_total_expense(1200, 400, 200, 300) 
# exercise.filter_transactions([250.0, 500.0, 75.0, 1000.0, 150.0], 200)


# do not change the code below
# Run unit tests automatically
main(module='test_module', exit=False)

file_path = 'test.txt'
success_number = extract_success_number(file_path)

if success_number == 5:
    email = input("Input your email")
    first_name = input("input your first name")
    last_name = input("input your last name")
    message = message="You passed all test for TIIDELAB Pre-Fellowship Python Class Assignment 2 on Control Structures and Functions"
    send_message(email, first_name, last_name, message)

