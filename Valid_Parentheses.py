"""
https://www.codewars.com/kata/6411b91a5e71b915d237332d
Write a function that takes a string of parentheses, and determines if the order of 
the parentheses is valid. The function should return true if the string is valid, and false 
if it's invalid.
Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

"""


def main(string):
    first_char = 0
    second_char = 0
    for character in string:
        if character == '(':
            first_char += 1
        if character == ')':
            second_char += 1
        if first_char < second_char:
            return False
    return first_char == second_char


if __name__ == "__main__":
    print(main("()"))
    print(main(")(()(())"))
    print(main("(())((()())())"))
    print(main("("))
