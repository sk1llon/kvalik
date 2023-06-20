list = []
max = 0
new_list = []
n = int(input('Введите кол-во видеокарт: '))
for a in range(n):
    print('Видеокарта',a + 1,':',end = '')
    card = int(input())
    list.append(card)
for i in list:
    if i > max:
        max = i
for b in list:
    if b != max:
        new_list.append(b)
print(new_list)

