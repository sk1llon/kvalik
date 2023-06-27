def sort():
    for i_new in range(len(new_class)):
        for current in range(len(new_class)):
            if new_class[i_new] < new_class[current]:
                new_class[i_new], new_class[current] = new_class[current], new_class[i_new]


first_class = []
second_class = []
new_class = []
for i_first in range(160, 177, 2):
    first_class.append(i_first)
for i_second in range(162, 181, 3):
    second_class.append(i_second)
new_class.extend(first_class)
new_class.extend(second_class)
sort()
print('Отсортированный список учеников:', new_class)
