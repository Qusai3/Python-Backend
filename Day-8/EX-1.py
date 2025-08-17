class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance  # private

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrew:", amount)
        else:
            print("Withdrawal denied.")

    def display_balance(self):
        print("Balance for", self.account_holder, "is", self.balance)
        return self.balance

    # helper for subclasses
    def _get_balance(self):
        return self.balance

    def _set_balance(self, new_value):
        self.balance = new_value

    # ----- magic methods -----
    def __str__(self):
        return f"Account({self.account_number}) - Holder: {self.account_holder}, Balance: {self.balance}"

    def __eq__(self, other):
        if not isinstance(other, Account):
            return False
        return self.account_number == other.account_number


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    # keep at least 100 after withdrawal
    def withdraw(self, amount):
        if amount > 0 and (self._get_balance() - amount) >= 100:
            self._set_balance(self._get_balance() - amount)
            print("Withdrew:", amount)
        else:
            print("Withdrawal denied (must keep minimum 100).")


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=200):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # allow negative balance down to -overdraft_limit
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        new_balance = self._get_balance() - amount
        if new_balance >= -self.overdraft_limit:
            self._set_balance(new_balance)
            print("Withdrew:", amount)
        else:
            print("Withdrawal denied (overdraft limit exceeded).")


s = SavingsAccount("SA100", "Alice", 300, 0.03)
c = CheckingAccount("CA200", "Bob", 50, 150)

print(s)                 
print(c)
print("Same account?", s == c)  

s.withdraw(220)          
s.withdraw(150)