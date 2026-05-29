#Topic: Encapsulation in Python

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)


# Creating object
acc = BankAccount("Amit", 5000)

acc.deposit(2000)
acc.withdraw(1500)

acc.show_balance()

# Trying to access private variable directly (will raise an error)
# print(acc.__balance)  # Uncommenting this line will raise an AttributeError