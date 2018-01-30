"""
Bridget Franciscovich
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    """
    This function returns a string value
    """
    a_string = 'Hello, my name is Bridget'
    return str(a_string)


def give_me_an_integer():
    """
    This function returns an integer value
    """
    year_born = 1991
    current_year = 2018
    age = current_year - year_born
    return int(age)    


def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    year_born = 1991
    current_year = 2018
    age = current_year - year_born
    if age < 21:
        return False
    else:
        return True

def give_me_a_float():
    """
    This function returns a float value
    """
    year_born = 1991
    current_year = 2018
    age = current_year - year_born
    age_pi = age * 3.14
    return float(age_pi)

def give_me_a_list():
    """
    This function returns a list
    """
    year_born = 1991
    current_year = 2018
    age = current_year - year_born
    age_pi = age * 3.14
    return [year_born, current_year, age, age_pi]

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    croatian = {}
    croatian['hello'] = 'pozdrav'
    croatian['hi'] = 'zdravo'
    croatian['my'] = 'moj'
    croatian['name'] = 'ime'
    croatian['is'] = 'je'
    croatian['mine'] = 'rudnik'
    croatian['your'] = 'svoje'
    croatian['yours'] = 'tvoje'
    croatian['Croatia'] = 'Hrvatska'
    croatian['beautiful'] = 'lijep'
    return croatian

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    low_score = 50
    high_score = 100
    score = 500
    if score > high_score:
        high_score = score
    elif score < low_score:
        low_score = score
    return (high_score, low_score)

def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    res = 0
    for i in range(11):
        res = res + i
    return res

def check_is_even(number):
    """
    This function returns True if num is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    res = 0
    if number % 2 == 0:
        return True
    else:
        return False

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """
    if number1 < number2:
        return True
    else:
        return False

# Grad student's were asked to create two other functions, these are mine!

def sum_range_five_to_hundred_by_five():
    """
    This function returns the sum of the numbers five to one hundred by 5's.
    returns: integer  
    """
    res = 0
    for i in range(5,101,5):
        res = res + i
    return res

def count_letters(word):
    """
    This function retuns the length of word.
    word: string
    Returns: integer value corresponding to length of word
    """
    res = 0
    for letter in word:
        res = res + 1
    return res
