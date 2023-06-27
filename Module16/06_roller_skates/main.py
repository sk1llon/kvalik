skates = []
peoples_legs = []
skates_amount = int(input('Введите кол-во коньков: '))
count = 0
for i in range(skates_amount):
    skates.append(int(input(f'Размер {i + 1}-й пары: ')))
people_amount = int(input('Введите кол-во человек: '))
for ii in range(people_amount):
    peoples_legs.append(int(input(f'Размер ноги {ii + 1}-го человека: ')))
for i_legs in peoples_legs:
    for a in range(len(skates)):
        if skates[a] >= i_legs:
            skates.remove(skates[a])
            count += 1
            break
print('Наибольшее кол-во людей, которые могут взять ролики:',count)
