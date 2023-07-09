def even(word, dct):
    flag = False
    for i_word in word:
        if i_word in dct:
            dct[i_word] += 1
        else:
            dct[i_word] = 1
    for values in dct.values():
        if values % 2 == 1:
            print('Нельзя сделать палиндром')
            flag = False
            break
        else:
            flag = True
    if flag:
        print('Можно сделать палиндром')


def odd(word, dct):
    flag = False
    count = 0
    for i_word in word:
        if i_word in dct:
            dct[i_word] += 1
        else:
            dct[i_word] = 1
    for values in dct.values():
        if values % 2 == 1:
            count += 1
        if count % 2 == 1:
            flag = True
    if flag:
        print('Можно сделать палиндром')
    else:
        print('Нельзя сделать палиндром')


dictionary = {}
string = input('Введите строку: ')
if len(string) % 2 == 0:
    even(string, dictionary)
else:
    odd(string, dictionary)
