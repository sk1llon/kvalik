def people_find(contacts):
    surname = input('Введите фамилию: ')
    for keys, values in contacts.items():
        if keys[1] == surname:
            print(keys[0], keys[1], contacts[keys])


def add_contact(contacts):
    name, surname = input('Введите имя и фамилию нового контакта (через пробел) ').split()
    if name and surname not in contacts:
        number = int(input('Введите номер телефона: '))
        contacts[name, surname] = number
        return contacts
    else:
        print('Такой контакт уже есть')


contacts_dictionary = {}
while True:
    choice = int(input('Введите номер действия: '
                       '\n1. Добавить контакт'
                       '\n2. Найти человека\n'))
    if choice == 1:
        contacts_dictionary = add_contact(contacts_dictionary)
        print('Текущий словарь контактов:', contacts_dictionary)
    elif choice == 2:
        people_find(contacts_dictionary)
    else:
        print('Такой команды нет. Попробуйте ещё раз.')