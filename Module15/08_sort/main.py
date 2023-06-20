sort_list = []
n = int(input('Введите кол-во чисел в списке: '))
for _ in range(n):
    digit = int(input('Введите число: '))
    sort_list.append(digit)
print('Изначальный список:',sort_list)
for i_sort in range(len(sort_list)):
    for n in range(i_sort, len(sort_list)):
        if sort_list[n] < sort_list [i_sort]:
            sort_list[n], sort_list[i_sort] = sort_list[i_sort], sort_list[n]
print('Отсортированный список:',sort_list)