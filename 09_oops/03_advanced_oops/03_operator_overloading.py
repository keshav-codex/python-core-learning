# Operator Overloading in Python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Display format
    def __str__(self):
        return f"({self.x}, {self.y})"


# Creating objects
p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2  # calls __add__()

print(p3)