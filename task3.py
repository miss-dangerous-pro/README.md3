# Taking input in Python
# Basic Input
name = input("Enter your name: ")
print("Hello, " + name + "!")
# Input as an Integer
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")
# Input as a Floating-Point Number
height = float(input("Enter your height in meters: "))
print("Your height is " + str(height) + " meters.")
# Converting Input to a Specific Type
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
# Input with Floating-Point Numbers
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)
# Handling Multiple Inputs
numbers = input("Enter three numbers separated by space: ").split()
num1 = int(numbers[0])
num2 = int(numbers[1])
num3 = int(numbers[2])
average = (num1 + num2 + num3) / 3
print("The average is:", average)
# Taking input from console in Python 
# Simple Console Input
# Taking name as input
name = input("Enter your name: ")

# Taking age as input
age = input("Enter your age: ")

# Printing a greeting message
print(f"Hello, {name}! You are {age} years old.")
#  Console Input with Data Conversion
# Taking two numbers as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Performing addition
sum = num1 + num2

# Printing the result
print(f"The sum of {num1} and {num2} is {sum}.")
# handling Multiple Inputs at Once
# Taking three numbers as input in one line
num1, num2, num3 = map(int, input("Enter three numbers separated by spaces: ").split())

# Calculating the average
average = (num1 + num2 + num3) / 3

# Printing the average
print(f"The average of the three numbers is {average:.2f}.")
# Taking multiple inputs from user in Python
# Multiple Inputs in One Line (Using split())
# Taking three numbers as input in one line
num1, num2, num3 = input("Enter three numbers separated by spaces: ").split()

# Converting the inputs to integers
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
#  Multiple Inputs in One Line (Using map())
# Taking three numbers as input in one line
num1, num2, num3 = map(int, input("Enter three numbers separated by spaces: ").split())

# Calculating the sum of the numbers
total = num1, + num2 + num3

# Printing the result
print(f"The sum of the numbers is: {total}.")
#  Multiple Inputs on Separate Lines
# Taking three numbers as input in one line
num1, num2, num3 = input("Enter three numbers separated by spaces: ").split()

# Converting the inputs to integers
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# Printing the numbers
print(f"The numbers you entered are: {num1}, {num2}, and {num3}.")
#  Multiple Inputs in One Line (Using map())
# Taking three numbers as input in one line
num1, num2, num3 = map(int, input("Enter three numbers separated by spaces: ").split())

# Calculating the sum of the numbers
total = num1, + num2 + num3

# Printing the result
print(f"The sum of the numbers is: {total}.")
# Multiple Inputs on Separate Lines
# Taking input on separate lines
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

# Printing the collected information
print(f"Name: {name}, Age: {age}, City: {city}")
#Taking Multiple Inputs and Storing Them in a List
# Taking an unknown number of inputs
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Printing the list of numbers
print("The numbers you entered are:", numbers)
# Taking Multiple Inputs with a Loop
# List to store inputs
numbers = []

# Number of inputs to take
n = int(input("How many numbers do you want to enter? "))

# Loop to take inputs
for _ in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Printing the list of numbers
print("The numbers you entered are:", numbers)

# Python | Output using print() function
# Example 1: Printing a string
print("Hello, World!")

# Example 2: Printing numbers
print(42)

# Example 3: Printing multiple items
print("The answer is", 42)

# Example 4: Printing variables
name = "vusqa"
age = 30
print("Name:", name, "Age:", age)

# Example 5: Printing with formatted strings (f-strings)
print(f"Name: {name}, Age: {age}")
# How to print without newline in Python?
print("hello!",end="")
print("orwa here!",end="")
print("whassup?","")
# Custom separator
print("Python", end=" -> ")
print("Programming")
# Python end parameter in print()
# Default behavior (end with a newline)
print("Hello")
print("World")

# Using the end parameter to stay on the same line
print("Hello", end="")
print("World")

# Using the end parameter to add a space instead of a newline
print("Hello", end=" ")
print("World")

# Using a custom string as the end parameter
print("Python", end=" -> ")
print("Programming")
# Python | sep parameter in print(
# Default separator (space)
print("Python", "is", "fun")

# Using sep to separate with a dash
print("Python", "is", "fun", sep="-")

# Using sep to separate with a custom string
print("Python", "is", "fun", sep=" * ")

# Using sep to separate with no space
print("Python", "is", "fun", sep="")
# Python | Output Formatting
# Using f-strings (formatted string literals)
name = "vusqa"
age = 30

# Basic f-string formatting
print(f"Name: {name}, Age: {age}")
#  Using str.format() Method
name = "vusqa"
age = 25

# Basic formatting
print("Name: {}, Age: {}".format(name, age))

# Positional and keyword arguments
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {name}, Age: {age}".format(name="Bob", age=25))

# Formatting numbers
pi = 3.14159265
print("Pi to two decimal places: {:.2f}".format(pi))
# Using % Operator (Old-style formatting)
name = "vusqa"
age = 28

# Basic formatting
print("Name: %s, Age: %d" % (name, age))

# Formatting numbers
pi = 3.14159265
print("Pi to two decimal places: %.2f" % pi)
# Using the pprint Module for Pretty Printing
import pprint

data = {'name': 'vusqa', 'age': 23, 'hobbies': ['reading', 'gaming', 'sleeping']}
pprint.pprint(data)
