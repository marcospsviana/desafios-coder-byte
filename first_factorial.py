"""
First Factorial
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.
Examples
Input: 4
Output: 24
Input: 8
Output: 40320
Tags

recursionmath fundamentalsfree
"""

def first_factorial(num):
    """
    >>> first_factorial(4)
    24
    >>> first_factorial(8)
    40320
    """
    factorial_result = 1
    for n in range(1, num + 1):
        factorial_result *= n

    return factorial_result