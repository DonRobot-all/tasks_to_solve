
# список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая фильтрует нечетные числа
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

# Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)

print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))




# Список строк с похожими элементами
list1 = ["Python", "CSharp", "Java", "Go"]
list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]

# функция, которая проверяет строки на вхождение
def filter_duplicate(string_to_check):
    if string_to_check in ll:
        return False
    else:
        return True

# Применение filter() для удаления повторяющихся строк
ll = list2
out_filter = list(filter(filter_duplicate, list1))
ll = list1
out_filter += list(filter(filter_duplicate, list2))

print("Отфильтрованный список:", out_filter)


# список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая фильтрует нечетные числа
def filter_odd_num(in_num):
    if in_num  > 10:
        return True
    else:
        return False

# Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)

print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))


# Список строк с похожими элементами
list1 = ["Python", "CSharp", "Java", "Go"]
list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]

# функция, которая проверяет строки на вхождение
def filter_duplicate(string_to_check):
    if 'a' in string_to_check:
        return True
    else:
        return False

# Применение filter() для удаления повторяющихся строк
out_filter = list(filter(filter_duplicate, list1))
out_filter2 = list(filter(filter_duplicate, list2))

print("Отфильтрованный список:", out_filter)
print("Отфильтрованный список:", out_filter2)