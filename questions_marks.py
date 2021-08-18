"""
Questions Marks
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, 
letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. 
If so, then your program should return the string true, otherwise it should return the string false. 
If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true 
because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true
"""

def questions_marks(sentence):
    """
    >>> questions_marks("aa6?9")
    'false'
    >>> questions_marks("acc?7??sss?3rr1??????5")
    'true'
    """
    number = 0
    questions = 0
    for s in sentence:
        if s.isnumeric():
            number += int(s)
        if number > 0 and s == '?':
            questions += 1
        if questions == 3 and number == 10:
            return 'true'
    if questions == 3 and number == 10:
        return 'true'
    else:
        return 'false'


