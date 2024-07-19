numb = int(input())
result = 0
while numb > 0:
    result += numb % 10
    numb = numb // 10

print(result)