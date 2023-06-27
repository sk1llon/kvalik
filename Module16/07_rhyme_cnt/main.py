circle = []
amount_of_people = int(input('Кол-во человек: '))
kick = int(input('Какое число выбывает: '))
index = 0
for i in range(1, amount_of_people + 1):
    circle.append(i)
while len(circle) != 1:
    print('Текущий круг людей:', circle)
    print('Начало счёта с номера', circle[index])
    delete = (index + kick - 1) % len(circle)
    if circle[delete] == circle[-1]:
        index = 0
    else:
        index = delete
    print('Выбывает человек под номером', circle.pop(delete))
print('Остался человек под номером', circle[0])