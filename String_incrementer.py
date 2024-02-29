"""
https://www.codewars.com/kata/54a91a4883a7de5d7800009c

Your job is to write a function which increments a string,
to create a new string.

If the string already ends with a number, the number should
be incremented by 1.
If the string does not end with a number. the number 1 should
be appended to the new string.
Examples:

foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
Attention: If the number has leading zeros the amount of digits should be considered.
water.

"""


def increment_string(strng):
    text = strng.rstrip('0123456789')
    numbers = strng[len(text):]
    if numbers == '':
        return strng + '1'
    return text + str(int(numbers) + 1).zfill(len(numbers))


if __name__ == "__main__":
    print(increment_string("foo"))
    print(increment_string("foobar001"))
    print(increment_string("foobar111"))
    print(increment_string("fo89obar001"))
    print(increment_string("foobar1"))
    print(increment_string(""))  # '1'
