# Method Overloading in Python

class Calculator:

    def add(self, *numbers):
        total = 0
        for num in numbers:
            total += num
        return total


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))
print(calc.add(1, 2, 3, 4, 5))