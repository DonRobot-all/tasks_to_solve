"""
https://www.codewars.com/kata/525f50e3b73515a6db000b83
Write a function that accepts an array of 10 integers (between 0 and 9), that
returns a string of those numbers in the form of a phone number.
Example

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!
   
"""

def create_phone_number(n):
    # s = ''.join(map(str, n))
    s = ''.join([str(i) for i in n])
    return f'({s[:3]}) {s[3:6]}-{s[6:]}'


def create_phone_number(n: list[int]) -> str:
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))