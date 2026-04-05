# This program searches for Python in my subjects list by using for else.

subjects = ["Math", "Science", "English", "History", "Python"]

for subject in subjects:
    if subject == "Python":
        print("Found Python")
        break
else:
    print("Python not found")