List = list(input('Введите слово: '))
reversedList = []
for a in reversed(List):
    reversedList.append(a)
if List == reversedList:
    print('Слово является палиндромом: ')
else:
    print('Слово не является палиндромом: ')