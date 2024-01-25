def scramble(number):
    total = 0
    while number:
        number //= 5
        print(f'число после деления {number}')
        total += number
    return total

if __name__ == "__main__":
    print(scramble(0))
    print(scramble(6))
    print(scramble(30))

