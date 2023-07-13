def function(dct):
    interests = []
    surnames = []
    surname_length = 0
    for i_dict in dct:
        interests.append(dct[i_dict]['interests'])
        surnames.append(dct[i_dict]['surname'])
    surnames = ''.join(surnames)
    for _ in surnames:
        surname_length += 1
    return interests, surname_length


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dictionary):
#     lst = []
#     string = ''
#     for i_dict in dictionary:
#         lst += (dictionary[i_dict]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)


for i_student in students:
    print('{0} - {1}'.format(i_student, students[i_student]['age']))
print('Полный список интересов всех студентов:', function(students)[0])
print('Общая длина всех фамилий студентов:', function(students)[1])


