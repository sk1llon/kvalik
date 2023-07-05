string = input('Введите строку: ').split()
maximum = 0
for i_str in string:
    if len(i_str) > maximum:
        maximum = i_str
print('Самое длинное слово:', maximum)
print('Длина этого слова:', len(maximum))

