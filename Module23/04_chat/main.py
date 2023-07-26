while True:
    chat = open('chat.txt', 'a', encoding='utf-8')
    account_name = input('Введите имя пользователя: ')
    action_choice = input('1. Посмотреть текущий текст чата.\n'
                          '2. Отправить сообщение.\n ')
    if action_choice == '1':
        chat.close()
        chat = open('chat.txt', 'r', encoding='utf-8')
        for i_line in chat:
            print(i_line, end='')
        chat.close()
    elif action_choice == '2':
        message = input('Введите сообщение: ')
        chat.write(account_name + ' : ' + message + '\n')
    else:
        print('Ошибка! Попробуйте ещё раз. ')
    chat.close()
