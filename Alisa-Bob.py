a = int(input())
winner = False
while a > 1:
    if a == 1:
        break
    print(a)
    a = a // 2
    if a % 2 != 0:
        winner = not winner
    print(winner)

if winner:
    print('Alisa')
else:
    print('Bob')

# if first % 2 == 0:
#     print("Bob")
# else:
#     print("Alisa")