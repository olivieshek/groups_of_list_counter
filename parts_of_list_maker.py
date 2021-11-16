students = [ВВЕДИТЕ СВОЙ СПИСОК]
students_length = len(students) # 7
group1_length = students_length / 2
if students_length % 2 == 1:
    group1_length += 0.5
group1_length = int(group1_length)
group2_length = int(students_length - group1_length)
group1 = []
group2 = []
def to_separate_List(list_name):
    i = 0
    for index, student in enumerate(students, 1):
        i += 1
        group1.append(student)
        if index >= group1_length:
            print('Первая группа сделана:', group1)
            break
    students.reverse()
    i = 0
    for index, student in enumerate(students, 1):
        i += 1
        group2.append(student)
        if index >= group2_length:
            group2.reverse()
            print('Вторая группа готова:', group2)
            return group1, group2;

to_separate_List(students)
print(group1, group2, '- получившиеся списки')