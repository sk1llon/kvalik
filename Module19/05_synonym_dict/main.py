amount_of_pairs = int(input('Введите количество пар слов: '))
pair_dictionary = dict()
for i in range(1, amount_of_pairs + 1):
    pairs = input('{0}-я пара: '.format(i)).lower().split(' - ')
    pair_dictionary[pairs[0]] = pairs[1]
    pairs.clear()
new_word = input('Введите слово: ')
word = pair_dictionary.get(new_word, 0)
if word == 0:
    while word == 0:
        print('Такого слова нет в словаре ')
        new_word = input('Введите слово: ')
        word = pair_dictionary.get(new_word, 0)
print('Синоним:', pair_dictionary.get(new_word))
