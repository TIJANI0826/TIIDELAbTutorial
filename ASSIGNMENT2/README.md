# Exercise Guide for Writing Financial Utility Functions

Welcome to the guide for writing the required functions to pass the provided test suite. Follow this guide to understand how to implement each function correctly. Let's dive into each function and see what is expected.

## Table of Contents
1. [Function 1: `balance_check`](#balance_check)
2. [Function 2: `calculate_interest`](#calculate_interest)
3. [Function 3: `check_loan_eligibility`](#check_loan_eligibility)
4. [Function 4: `filter_transactions`](#filter_transactions)
5. [Function 5: `calculate_total_expense`](#calculate_total_expense)
6. [Running the Tests](#running_the_tests)

<a name="balance_check"></a>
## 1. Function: `balance_check`
### Description:
Checks the balance after attempting to withdraw a specified amount. If the withdrawal amount is greater than the available balance, it should return the original balance and a message indicating insufficient funds. Otherwise, it should deduct the withdrawal amount from the balance and return the remaining balance along with a success message.

### Signature:
```python
def balance_check(balance: float, withdrawal_amount: float) -> tuple:
```
Parameters:
- `balance` (float): The current account balance.
- `withdrawal_amount` (float): The amount to withdraw.
### Returns:
- `tuple`: A tuple containing the updated balance and a message string.

### Sample Input
```python
balance_check(1000, 500)
balance_check(1000, 1500)
```
### Sample Ouput
```
(500, 'Withdrawal successful!')
(1000, "Insufficient funds.")
```

## 2. Function: `calculate_interest`
### Description:
Calculates the simple interest earned on a principal amount over a period of time at a given annual interest rate.

### Signature:
```python
def calculate_interest(principal: float, rate: float, time: float) -> float:
```

Parameters:
- `principal` (float): The initial amount of money.
- `rate` (float): The annual interest rate (as a percentage).
- `time` (float): The time period for which the interest is calculated (in years).

### Returns:
- `float`: The calculated interest.


### Sample Input
```python
calculate_interest(1000, 5, 1)
calculate_interest(2000, 3.5, 2)
```
### Sample Output
```
50
140
```

## 3. Function: `check_loan_eligibility`
### Description:
Checks if an individual is eligible for a loan based on their age, income, and credit score.

### Signature:
```python
def check_loan_eligibility(age: int, income: float, credit_score: int) -> str:
```

### Parameters:
- `age` (int): The age of the individual.
- `income` (float): The annual income of the individual.
- `credit_score` (int): The credit score of the individual.

### Returns:
- `str`: A message indicating whether the individual is eligible for a loan or not.

### Eligibility Criteria:
- Age must be at least 21.
- Income must be at least 30,000.
- Credit score must be at least 700.

### Sample Input
```python
check_loan_eligibility(25, 35000, 720)
check_loan_eligibility(20, 40000, 750)
check_loan_eligibility(30, 25000, 710)
check_loan_eligibility(40, 45000, 680)
```
### Sample Output
```
"Eligible for a loan."
"Not eligible for a loan."
"Not eligible for a loan."
"Not eligible for a loan."
```

## 4. Function: `filter_transactions`
### Description:
Filters a list of transactions to include only those above a specified threshold amount.

### Signature:
```python
def filter_transactions(transactions: list, threshold: float) -> list:
```
### Parameters:
- `transactions` (list): A list of transaction amounts.
- `threshold` (float): The threshold amount.

### Returns:
- `list`: A list of transactions that are above the threshold amount.

### Sample Input
```python
filter_transactions([250.0, 500.0, 75.0, 1000.0, 150.0], 200)
filter_transactions([100.0, 200.0, 300.0], 250)
filter_transactions([50.0, 60.0, 70.0], 100)
```
### Sample Output
```
[250.0, 500.0, 1000.0]
[300.0]
[]
```


## 5. Function: `calculate_total_expense`
### Description:
Calculates the total monthly expenses based on different categories.

### Signature:
```python
def calculate_total_expense(rent: float, groceries: float, utilities: float, entertainment: float) -> float:
```
### Parameters:
- `rent` (float): The monthly rent expense.
- `groceries` (float): The monthly groceries expense.
- `utilities` (float): The monthly utilities expense.
- `entertainment` (float): The monthly entertainment expense.
### Returns:
- `float`: The total monthly expense.

### Sample Input
```python
calculate_total_expense(1000, 300, 150, 200)
calculate_total_expense(800, 250, 100, 150)
calculate_total_expense(1200, 400, 200, 300) 
```
### Sample Output
```
1650
1300
2100
```


## Running the Tests
1. Implement the required functions in a file named exercise.py.
2. Open a terminal and navigate to the directory containing the files.
3. Run the tests using the following command:
```bash
python main.py
```
If your implementations are correct, all tests should pass, indicating that your functions work as expected.

Good luck with your coding!</a>

## Running the Tests
1. Implement the required functions in a file named exercise.py.
2. Open a terminal and navigate to the directory containing the files.
3. Run the tests using the following command:
```bash
python main.py
```
If your implementations are correct, all tests should pass, indicating that your functions work as expected.

Good luck with your coding!">

## Running the Tests
1. Implement the required functions in a file named exercise.py.
2. Open a terminal and navigate to the directory containing the files.
3. Run the tests using the following command:
```bash
python main.py
```
If your implementations are correct, all tests should pass, indicating that your functions work as expected.

Good luck with your coding!