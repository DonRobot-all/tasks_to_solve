"""
https://www.codewars.com/kata/530e15517bc88ac656000716

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in 
the alphabet. ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or 
special characters included in the string, they should be returned as they are. Only letters from the 
latin/english alphabet should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.

"""


# def rot13(message):
#     result = ''
#     for char in message:
#         if char.islower():
#             if char.isalpha():
#                 new_code = ord(char)
#                 if new_code <= 109:
#                     new_code += 13
#                 else:
#                     new_code -= 13
#                 result += chr(new_code)
#         elif char.isupper():
#             if char.isalpha():
#                 new_code = ord(char)
#                 if new_code <= 77:
#                     new_code += 13
#                 else:
#                     new_code -= 13
#                 result += chr(new_code)
#         else:
#             result += char
#     return result

# def rot13(message):
#     result = ''
#     for char in message:
#         result += (
#             chr(ord(char) + 13) if char.islower() and ord(char) <= 109
#             else chr(ord(char) - 13) if char.islower() and ord(char) > 109
#             else '')
#         result += (
#             chr(ord(char) + 13) if char.isupper() and ord(char) <= 77
#             else chr(ord(char) - 13) if char.isupper() and ord(char) > 77
#             else '')
#         result += char if not char.isalpha() else ''
#     return result


def rot13(message):
    result = ''
    for char in message:
        if (ord(char) >= ord('A') and ord(char) <= ord('M') or ord(char) >= ord('a') and ord(char) <= ord('m')):
            result += chr(ord(char) + 13)
        elif (ord(char) >= ord('M') and ord(char) <= ord('Z') or ord(char) >= ord('m') and ord(char) <= ord('z')):
            result += chr(ord(char) - 13)
        else:
            result += char
    return result


if __name__ == "__main__":
    print(rot13('test'))  # 'grfg'
    print(rot13(('Test')))  # 'Grfg'
    print(rot13('aA bB zZ 1234 *!?%'))  # 'nN oO mM 1234 *!?%'
