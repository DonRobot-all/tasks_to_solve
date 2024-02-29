"""
https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
Write a function named first_non_repeating_letter† that takes a string input, 
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the 
string.

As an added challenge, upper- and lowercase letters are considered the same
character, but the function should return the correct case for the initial
letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty
string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons,
but your function should handle any Unicode character.

"""


# def first_non_repeating_letter(s):
#     for char in s:
#         if s.lower().count(char.lower()) == 1:
#             return char
#     return ''


def first_non_repeating_letter(s):
    array = [char for char in s if s.lower().count(char.lower()) == 1]
    return array[0] if array else ''


if __name__ == "__main__":
    print(first_non_repeating_letter('a'))        # a
    print(first_non_repeating_letter('stress'))   # t
    print(first_non_repeating_letter('moonmen'))  # e
    print(first_non_repeating_letter(''))
    first_non_repeating_letter('abba')
