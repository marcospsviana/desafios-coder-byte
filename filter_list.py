def filter_list(l):
    """
    >>> filter_list([1,2,'a','b'])
    [1, 2]
    >>> filter_list([1,'a','b',0,15])
    [1, 0, 15]
    >>> filter_list([1,2,'aasf','1','123',123])
    [1, 2, 123]
    """
    for n in l:

        if (str(n)).isnumeric():
            set_numbers.add(int(n))
    set_numbers.remove('')
        
    return list(set_numbers)

