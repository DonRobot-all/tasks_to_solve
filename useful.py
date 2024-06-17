# help(print)

string = 'Helloareallthelettershere'
bool = string.isalpha()
print(bool)

students = {
    'Alex': 'not Alabuga',
    'Serg': 'Alabuga',
    'Timofei': 'Alabuga',
    'Valerii': 'dont know'
}

# списковое включение
result = dict((student, place) for student, place in students.items())
print(result)
# словарное включение
result = {student: place for student, place in students.items()}
print(result)