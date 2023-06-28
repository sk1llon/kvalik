# numbers = [[i for i in range(1, 12, 4)],
#            [i for i in range(2, 12, 4)],
#            [i for i in range(3, 12, 4)],
#            [i for i in range(4, 12, 4)]]
# print(numbers)
beginning = int(input('С какого числа начинаем? '))
ending = int(input('Каким числом заканчиваем? '))
main_length = int(input('Сколько значений в списке? '))
length = int(input('Сколько значений в одном значении? '))
first_list = [i for i in range(beginning, ending + 1)]
second_list = []
for index in range(main_length):
    memory = [i for i in range(beginning, ending + 1, main_length)]
    second_list.insert(index, memory)
    memory = []
    beginning += 1
print(second_list)
