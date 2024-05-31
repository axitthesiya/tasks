# Class to represent a bank account with a unique account number and balance
class Account:
    # Static variable to generate unique account numbers
    _account_number_seed = 9000789620  

    # Initialize the account with a unique account number and initial balance
    def __init__(self):
        # Initialize account number and balance
        self.account_number = Account._account_number_seed
        # Increment the account number seed for the next account
        Account._account_number_seed = 1000025896
        # Initialize the balance to 0.00
        self.balance = 00.00

    # Method to deposit money into the account
    def deposit(self, amount):
        # Check if the deposit amount is positive
        if amount > 0:
            # Add the deposit amount to the balance
            self.balance += amount
            # Print a message indicating the deposit and new balance
            print(f"Deposited {amount:.2f}/-        | New balance is {self.balance:.2f}/-")
        else:
            # Print an error message if the deposit amount is not positive
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        # Check if the withdrawal amount is positive and within the available balance
        if 0 < amount <= self.balance:
            # Subtract the withdrawal amount from the balance
            self.balance -= amount
            # Print a message indicating the withdrawal and new balance
            print(f"Withdrew {amount:.2f}/-          | New balance is {self.balance:.2f}/-")
        else:
            # Print an error message if the withdrawal amount is not valid
            print("Withdrawal amount must be positive and within the available balance.")

    # Method to represent the account as a string
    def __str__(self):
        # Return a string representation of the account
        return f"Account Number: {self.account_number}, Balance: {self.balance:.2f}/-"


# Class to represent a savings account with an interest rate
class SavingsAccount(Account):
    # Initialize the savings account with an interest rate
    def __init__(self, interest_rate):
        # Call the parent class constructor
        super().__init__()
        # Initialize the interest rate
        self.interest_rate = interest_rate

    # Method to calculate and add interest to the balance
    def calculate_interest(self):
        # Calculate the interest amount
        interest = self.balance * (self.interest_rate / 100)
        # Add the interest to the balance
        self.balance += interest
        # Print a message indicating the interest and new balance
        print(f"Calculated interest {interest}   | New balance is {self.balance:.2f}/-")

    # Method to represent the savings account as a string
    def __str__(self):
        # Return a string representation of the savings account
        return f"Savings {super().__str__()}, Interest Rate: {self.interest_rate}%"


# Class to represent a current account with an overdraft limit
class CurrentAccount(Account):
    # Initialize the current account with an overdraft limit
    def __init__(self, overdraft_limit):
        # Call the parent class constructor
        super().__init__()
        # Initialize the overdraft limit
        self.overdraft_limit = overdraft_limit

    # Method to withdraw money from the account
    def withdraw(self, amount):
        # Check if the withdrawal amount is positive and within the available balance and overdraft limit
        if 0 < amount <= self.balance + self.overdraft_limit:
            # Subtract the withdrawal amount from the balance
            self.balance -= amount
            # Print a message indicating the withdrawal and new balance
            print(f"Withdrew {amount:.2f}/-         | New balance is {self.balance:.2f}/-")
        else:
            # Print an error message if the withdrawal amount is not valid
            print(f"Withdrawal amount exceeds the overdraft limit. Available balance: {self.balance:.2f}/- | Overdraft limit: {self.overdraft_limit}/-")

    # Method to represent the current account as a string
    def __str__(self):
        # Return a string representation of the current account
        return f"Current {super().__str__()}, Overdraft Limit: {self.overdraft_limit}/-"

# Example usage:
savings = SavingsAccount(5)  # 5% interest rate
print(savings)
savings.deposit(1000)
savings.calculate_interest()
savings.withdraw(200) 
print()

current = CurrentAccount(500)  # 500 overdraft limit
print(current)
current.deposit(500)
current.withdraw(900) # Withdrawing 900  (exceeding overdraft limit)