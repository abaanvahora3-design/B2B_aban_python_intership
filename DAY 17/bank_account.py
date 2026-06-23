class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}.")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}.")
        else:
            print("Withdraw amount must be positive.")
            
    def display_balance(self):
        print(f"Balance: {self.balance}")

print("--- Creating Account ---")
account = BankAccount(1000)
account.display_balance()

print("\n--- Transactions ---")
account.deposit(4500)
account.withdraw(500)
account.withdraw(10000) # Should fail

print("\n--- Final Status ---")
account.display_balance()
