# Assignment 1
# This file contains the introduction to python. Focusing on the basics of the language such as variables, operators 
# and conditional statements. 

# Task 1: Introduction to Variables

# Declaration and initalization of variables 
name = 'Kimone'
age = 22
height = 5.2

# Prints an introduction message
# Uses 'f' and curly braces to print the values of the varibles. This makes the code more readable. 
print(f"Hey there, my name is {name}! I'm {age} years old and I'm {height} feet tall.")

# Task 2: Introduction to operators

# Variable declaration and initialization
num1 = 357
num2 = 28

# Calculates and prints the results of each operation
print(f"The sum of {num1} and {num2} is ", num1+num2)
print(f"The product of {num1} and {num2} is ", num1*num2)
print(f"The difference of {num1} and {num2} is ", num1-num2)
print(f"The quotient of {num1} and {num2} is ", num1/num2)

# Task 3: Conditional Statements

# Get input from user
user_input = int(input("Enter a number: "))

# Checks if the number is positive, negative or 0
if user_input>0:
    print("The number is positive. Awesome!")
elif user_input<0:
    print("The number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")
