"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"""

def to_camel_case(text):
    """
    >>> to_camel_case('the-stealth-warrior')
    'theStealthWarrior'
    >>> to_camel_case('The_Stealth_Warrior')
    'TheStealthWarrior'
    >>> to_camel_case('A-Cat_was_kawaii')
    'ACatWasKawaii'
    >>> to_camel_case('a_Pippi-was_cute')
    'aPippiWasCute'
    >>> to_camel_case('a_Cat-Was-Pippi')
    'aCatWasPippi'
    >>> to_camel_case('A-Cat_was_pippi')
    'ACatWasPippi'
    >>> to_camel_case('A_pippi-is_Savage')
    'APippiIsSavage'
    >>> to_camel_case('a_cat-Was-evil')
    'aCatWasEvil'
    >>> to_camel_case('A_Pippi_Was_cute')
    'APippiWasCute'
    >>> to_camel_case('the_Cat-was_cute')
    'theCatWasCute'
    """
    camel_case_text = ''
    lista = text.replace('-', ' ').replace('_', ' ').split()
    
    if not lista[0].istitle():
        camel_case_text = lista[0]
    else:
        camel_case_text = lista[0].capitalize()
    for texto in lista[1:]:
        camel_case_text += texto.capitalize()
    return camel_case_text