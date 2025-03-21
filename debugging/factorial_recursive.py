#!/usr/bin/python3
import sys

# Function Description:
# The factorial function calculates the factorial of a given number 'n' recursively.
# Factorial of a number 'n' is defined as the product of all positive integers less than or equal to n.
# For example, factorial(4) = 4 * 3 * 2 * 1 = 24.
# The base case is when n equals 0, in which case the function returns 1, as the factorial of 0 is 1.

# Parameters:
#   n (int): The number for which we want to calculate the factorial.
#            The function will recursively call itself with n-1 until n reaches 0.

# Returns:
#   int: The factorial of the number 'n'. If n is 0, the function returns 1.
#        For any other positive integer, it returns n * factorial(n-1).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Main section of the script:
# The script takes an integer input from the command line argument, calculates its factorial using the 
# factorial function, and prints the result.

f = factorial(int(sys.argv[1]))  # Get the argument passed and call the factorial function
print(f)  # Output the result

