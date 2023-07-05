digit_count = 0
upper_count = 0
while True:
    password = input('Придумайте пароль: ')
    for i_pass in password:
        if i_pass.isupper():
            upper_count += 1
    for i_pass in password:
        if i_pass.isdigit():
            digit_count += 1
    if len(password) >= 8 and upper_count >= 1 and digit_count >= 3:
        print('Пароль надёжный!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз')
