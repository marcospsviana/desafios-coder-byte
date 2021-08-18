def square_digits(num):
    """
    >>> square_digits(9119)
    811181
    >>> square_digits(0)
    0
    """
    nums = ''
    for n in str(num):
        nums += str(int(n)* int(n))
    return int(nums)
