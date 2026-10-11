# Day 2 - Python Basics

# 1. Variables and data types
name = "Rahul"
age = 21
salary = 25000.0
is_student = True

print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Is student:", is_student)

# 2. List
numbers = [10, 20, 30, 40]
print("\nList:", numbers)
numbers.append(50)
print("After adding:", numbers)

# 3. Tuple
colors = ("red", "green", "blue")
print("\nTuple:", colors)

# 4. Set - stores unique values
unique_numbers = {1, 2, 2, 3, 4}
print("\nSet:", unique_numbers)

# 5. Dictionary
student = {"name": "Rahul", "marks": 85}
print("\nDictionary:", student)

# 6. Conditions
if age >= 18:
    print("\nAdult")
else:
    print("\nMinor")

# 7. Loops
print("\nNumbers:")
for number in numbers:
    print(number)

# 8. Function
def add(a, b):
    return a + b

print("\nSum:", add(10, 20))

# 9. Lambda
multiply = lambda a, b: a * b
print("Multiplication:", multiply(5, 4))

# 10. List comprehension
squares = [n * n for n in numbers]
print("Squares:", squares)

# 11. Exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 12. File handling
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python file handling.")

with open("sample.txt", "r", encoding="utf-8") as file:
    print("\nFile content:", file.read())

# 13. Class and object
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name, "Salary:", self.salary)

employee = Employee("Amit", 30000)
employee.display()

print("\nPython basics completed.")