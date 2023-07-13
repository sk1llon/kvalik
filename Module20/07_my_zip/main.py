string = input('Введите строку: ')
new_tuple = input('Введите кортеж: ').split(', ')
new_string = zip(string, new_tuple)
for i_str in new_string:
    print(i_str)
