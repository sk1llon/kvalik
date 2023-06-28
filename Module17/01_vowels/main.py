text = input('Введите текст: ')
vowels = 'аеёиоуыэюя'
List = [i for i in text if i in vowels]
print('Список гласных букв:', List)
print('Длина списка:', len(List))
