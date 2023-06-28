string = input('Введите строку: ')
first = string.index('h')
second = 0
for index in range(first + 1, len(string)):
    if string[index] == 'h':
        second = index
print('Развёрнутая последовательность между первым и последним h:',
      string[second - 1:first:-1])

