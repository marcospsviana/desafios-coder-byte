"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
Example

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

"""

def create_phone_number(n):
    """
    >>> create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    '(123) 456-7890'
    >>> create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])
    '(023) 056-0890'
    """
    numbers_phone = ''.join(str(x) for x in n)
    return f'({numbers_phone[0:3]}) {numbers_phone[3:6]}-{numbers_phone[6:]}'

   