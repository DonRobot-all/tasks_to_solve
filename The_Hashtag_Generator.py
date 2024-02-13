"""
https://www.codewars.com/kata/52449b062fb80683ec000024

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false



"""


# def generate_hashtag(s):
#     result = '#'
#     for i in s.split():
#         result += i.capitalize()
#     return False if len(s) == 0 or len(result) > 140 else result


def generate_hashtag(s):
    result = '#'
    first = 0
    second = 0
    for i in s:
        second += 1
        if not i.isalpha() or second == len(s):
            result += s[first:second].capitalize().replace(' ', '')
            first = second
    return False if len(s) == 0 or len(result) > 140 else result


if __name__ == "__main__":
    print(generate_hashtag('Codewars'))
    print(generate_hashtag('Codewars      '))
    print(generate_hashtag('Codewars Is Nice'))
    print(generate_hashtag('CoDeWaRs is niCe'))  #CodewarsIsNice
    print(generate_hashtag('c i n'))
    print(generate_hashtag(''))
