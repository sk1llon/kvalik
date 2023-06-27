a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
count = 0
for i_list in a:
    if i_list == 5:
        count += 1
        a.remove(i_list)
print('Кол-во цифр 5 при первом объединении:', count)
count = 0
a.extend(c)
for i_second_list in a:
    if i_second_list == 3:
        count += 1
        a.remove(i_second_list)
print('\nКол-во цифр 3 при втором объединении:', count)
print(a)
