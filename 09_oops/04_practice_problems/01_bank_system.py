# Bank System using OOP

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0")
            return

        self.balance += amount
        print(f"{amount} deposited successfully")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0")
            return

        if amount > self.balance:
            print("Insufficient balance")
            return

        self.balance -= amount
        print(f"{amount} withdrawn successfully")

    def get_balance(self):
        return self.balance

    def show_details(self):
        print("----- Account Details -----")
        print("Holder:", self.account_holder)
        print("Balance:", self.balance)


# ---------------- Test Code ----------------

acc1 = BankAccount("Amit", 1000)

acc1.deposit(500)
acc1.withdraw(300)

print("Current Balance:", acc1.get_balance())

acc1.show_details()