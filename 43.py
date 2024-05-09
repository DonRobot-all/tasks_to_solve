a = [2]
b = a
print(id(a), id(b))


a = [2]
a[:] = a
print(id(a), id(b))