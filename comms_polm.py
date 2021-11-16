students = ['Alex', 'Bunny', 'Curly', 'Dan', 'Ethan', 'Fire', 'Graham']
testing_group1 = ['Alex', 'Bunny', 'Curly', 'Dan']
testing_group2 = ['Ethan', 'Fire', 'Graham']
students_length = len(students) # 7
group1_length = students_length / 2 # 3.5
if students_length % 2 == 1: # True / False
    group1_length += 0.5 # 3.5 + 0.5 = 4.0
group1_length = int(group1_length) # 4
print('Длина первой группы:', group1_length) # 4
group2_length = int(students_length - group1_length) # 7 - 4 = 3
print('Длина второй группы:', group2_length ) # 3
group1 = []
group2 = []
def to_separate_List(list_name):
    i = 0
    for index, student in enumerate(students, 1):
        i += 1
        print(student, f'- итерация номер {i}')
        group1.append(student)
        if index >= group1_length:
            print('The first group is done! Here is', group1)
            break
    students.reverse()
    print(students, '- результат после оператора .reverse()')
    i = 0
    for index, student in enumerate(students, 1):
        i += 1
        print(student, f'- итерация номер {i}')
        group2.append(student)
        if index >= group2_length:
            group2.reverse()
            print('The second group is done too! Here is', group2)
            return group1, group2;

separated = to_separate_List(students)
print(group1, group2, '- отдельно взятые переменные (списки)')
print(separated, '- итог функции to_separate_List(students)')

def to_review_Groups(first_group, second_group):
    print(f'Проверим первую группу {first_group}')
    if group1 == testing_group1:
        first_rev = 'Первая группа правильна!'
    else:
        first_rev = 'Первая группа НЕправильна!'
    print(f'Проверим вторую группу {second_group}')
    if group2 == testing_group2:
        second_rev = 'Вторая группа правильна!'
    else:
        second_rev = 'Вторая группа НЕправильна!'
    return first_rev, second_rev

print(to_review_Groups(group1, group2))