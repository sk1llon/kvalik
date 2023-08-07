class Students:

    def __init__(self, name, group_number, gpa):
        self.name = name
        self.group_number = group_number
        self.GPA = gpa

    def print_info(self):
        print('Name: ' + self.name, 'Group number: ' + str(self.group_number), 'GPA: ' + str(self.GPA), sep='\n')

    def give_average(self):
        return self.GPA


def grade_point_average(marks):
    sum_of_marks = 0
    for i_mark in marks:
        sum_of_marks += int(i_mark)
    avg = sum_of_marks / 5
    return avg


def receiving_data():
    name = input('Введите ФИ: ')
    group = int(input('Введите номер группы: '))
    student_marks = input('Введите оценки через пробел: ').split()
    gpa = grade_point_average(student_marks)
    return name, group, gpa


students_list = [Students(*receiving_data()) for _ in range(4)]
students_list.sort(key=lambda x: x.give_average(), reverse=True)
for i_student in students_list:
    print()
    i_student.print_info()
