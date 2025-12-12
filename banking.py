import time
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Deposits into the bank account
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}")

    # Withdraw money from the bank account
    def withdraw(self, amount):
        self.balance -= amount
        print(f"{self.owner} withdrew ${amount}")
    # Shows current balance
    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")

# Def which account to access
def ask_account(account1, account2):
    while True:
        try:
            print("Which account would you like to access?(1 or 2)")
            print(f"1. {account1.owner}\'s account")
            print(f"2. {account2.owner}\'s account")
            choice = input("Please select an option:  ").strip()
            if choice == "1":
                make_account_changes(account1)
                break
            if choice == "2":
                make_account_changes(account2)
                break
            print("Please enter in a valid choice.")
        except ValueError:
            "Please enter in a valid digit"
def make_account_changes(account):
    while True:
        try:
            print(f"You are accessing {account.owner}\'s account.")
            print("Select an option to choose from:")
            print("1. Make a deposit")
            print("2. Make a withdrawl")
            print("3. Check the current account balance.")
            choice = input("Please select an option:  ").strip()
            if choice == "1":
                amount = int(input("Please enter the amount to deposit").strip())
                account.deposit(amount)
                account.balance
                break
            if choice == "2":
                amount = int(input("Please enter the amount to withdraw").strip())
                account.balance
                break
            if choice == "3":
                account.show_balance()
                break
        
        # Error handling
            print("Please enter in a valid choice.")
            time.sleep(2)
        except ValueError:
            "Please enter in a valid number"

def main():
    account1 = BankAccount(owner= "Jacob", balance= 500)
    account2 = BankAccount(owner="Mom", balance=500)
    ask_account(account1, account2)
if __name__ == "__main__":
    main()