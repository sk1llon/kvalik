string = input('Введите строку: ')
count = 1
new_string = []
for i_str in range(len(string)):
    if string[i_str] == string[i_str + 1]:
        count += 1
    else:
        new_string.extend(string[i_str])
        new_string.extend(str(count))
        count = 1
print(''.join(new_string))
