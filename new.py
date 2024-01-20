tyt_input = input().lower()   # этот .lower() просто имба

slova = tyt_input.split()  

krytoi_slovarik = {}  # самый изящный словарь
for bykva in slova:  # любимый for чтобы научится бегать
    if bykva not in krytoi_slovarik:  # Если тут чёт новое то радуемся
        krytoi_slovarik[bykva] = 1  # И добавляем в наш словарный запас
    else:
        krytoi_slovarik[bykva] += 1  # А если нет то грустим и добавляем один чтобы менее грустить

print(krytoi_slovarik) # а тут выдаём чо мы тут нахимичили


# diction = {
#     'Валерий': 14,
#     'Александр': 15,
#     'Костя': 17
# }
# diction['Костя'] = 12
# print(diction)
# print(diction.setdefault('Костя', 15))
# print(diction)
# del diction['Валерий']
# print(diction)
# print(diction['Александр'])
# print(diction.get('Александр'))
# print(diction.keys())
# print(diction.values())
# print(diction.items())
# print(diction.popitem())
# print(diction.pop('Александр'))
# diction.clear()
# print(diction)


# name = 'Олег'
# if name in diction:
#     print(f'{name}, есть в словаре')
# else:
#     print(f'{name}, нет в словаре')

# def example(word):
#     return word[1]

diction = {
    'Валерий': -20,
    'Александр': 15,
    'Костя': 17
}
# print(diction.items()[0])
for key, value in diction.items():
    print(key, value)

# print(sorted(diction))  # reverse=True
# print(sorted(diction.values())) 
# print(sorted(diction, key=len)) 
# print(sorted(diction.values())) 
# print(sorted(diction.values(), key=abs)) 
# print(sorted(diction, key=example)) 



# Условие

# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно 
# встречалось в этом тексте ранее.

# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим 
# числом пробелов или символами конца строки.

# one two one tho three
# one: 2
# two: 1
# tho: 1
# three:1



# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye

