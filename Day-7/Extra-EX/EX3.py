class BankAccount:
    def __init__(self, account_holder, balance=0):  # Fixed constructor name
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrew:", amount)
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

acc = BankAccount("Alice")
acc.deposit(100)
acc.withdraw(50)
print("Balance:", acc.get_balance())
acc.withdraw(100)