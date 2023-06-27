guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
guest = ''
while guest != 'Пора спать':
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    guest = input('Гость пришёлл или ушёл? ')
    if guest == 'Пришёл':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            guests.append(name)
            print('Привет', name)
        else:
            print('Прости,' + name + ',мест нет')
    if guest == 'Ушёл':
        name = input('Имя гостя: ')
        guests.remove(name)
        print('Пока', name)
print('Вечеринка закончилась, все легли спать')