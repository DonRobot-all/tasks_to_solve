"""
https://www.codewars.com/kata/55c6126177c9441a570000cc
My friend John and I are members of the "Fat to Fit Club (FFC)". John is 
worried because each month a list with the weights of members is 
published and each month he is the last on the list which means he is 
the heaviest.

I am the one who establishes the list so I told him: "Don't worry any
more, I will modify the order of the list". It was decided to attribute
a "weight" to numbers. The weight of a number will be from now on the
sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in
the list 100 will come before 99.

Given a string with the weights of FFC members in normal order can
you give this string ordered by "weights" of these numbers?
Example:

"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:
 11 11 11  1  18 14 14  9   9

"100 180 90 56 65 74 68 86 99"

When two numbers have the same "weight", let us class them as if
they were strings (alphabetical ordering) and not numbers:

180 is before 90 since, having the same "weight" (9), it comes
before as a string.

All numbers in the list are positive numbers and the list can
be empty.

"""


def sort_rule(number):
    return sum([int(i) for i in number])


def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()), key=sort_rule))


if __name__ == "__main__":
    print(order_weight("103 123 4444 99 2000"))
    print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
                     # '11 11 2000 10003 22 123 1234000 44444444 9999'
    print(order_weight(""))
