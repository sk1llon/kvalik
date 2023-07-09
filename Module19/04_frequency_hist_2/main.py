def dictionary(string):
    text_dict = dict()
    for symbol in string:
        if symbol in text_dict:
            text_dict[symbol] += 1
        else:
            text_dict[symbol] = 1
    return text_dict


text = input('Введите текст: ').lower()
dictionary_list = dictionary(text)
for keys, values in sorted(dictionary_list.items()):
    print(keys, ':', values)
set_dictionary = sorted(set(dictionary_list.values()))
print('--------')
for i_set in set_dictionary:
    for keys, values in sorted(dictionary_list.items()):
        if values == i_set:
            print('{0} : {1}'.format(values, keys))
