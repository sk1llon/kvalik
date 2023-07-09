amount_of_orders = int(input('Введите кол-во заказов: '))
dictionary = {}
for i_order in range(1, amount_of_orders + 1):
    order = input('Введите {0}-й заказ: '.format(i_order))
    surname, pizza, amount = order.split()
    amount = int(amount)
    if surname not in dictionary:
        dictionary[surname] = {pizza: amount}
    else:
        if pizza not in dictionary[surname]:
            dictionary[surname] |= {pizza: amount}
        else:
            dictionary[surname][pizza] += amount
for surname, order in sorted(dictionary.items()):
    print('{0}:'.format(surname))
    for pizza, amount in sorted(order.items()):
        print('     {0}: {1}'.format(pizza, amount))
