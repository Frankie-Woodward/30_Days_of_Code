"""To complete this challenge, you must save a line of input 
from stdin to a variable, print Hello, World. on a single line, 
and finally print the value of your variable on a second line."""

# "Day 1"
# # Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
# input_string = input()

# # Print a string literal saying "Hello, World." to stdout.
# print('Hello, World.')

# # TO-DO: Write a line of code here that prints the contents of input_string to stdout.

# "Day 2"
# # Declare 3 variables: one of type int, one of type double, and one of type String.

# # The first line contains an integer that you must sum with i.
# # The second line contains a double that you must sum with d.
# # The third line contains a string that you must concatenate with s.
# i = 4
# d = 4.0
# s = 'HackerRank '
# # Declare second integer, double, and String variables.

# # Read and save an integer, double, and String to your variables.
# num = int(input())
# afloat = float(input())
# astring = input()
# # Print the sum of both integer variables on a new line.
# print(num + int(i))
# print(afloat + d)
# # Print the sum of the double variables on a new line.
# print(s + astring)
# # Concatenate and print the String variables on a new line
# # The 's' variable above should be printed first.

"Day 3"

"""Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being 
added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, 
find and print the meal's total cost. Round the result to the nearest integer."""

# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    return round((meal_cost) + ((tip_percent/100)*meal_cost) + (tax_percent/100)*meal_cost)

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    print(solve(meal_cost, tip_percent, tax_percent))