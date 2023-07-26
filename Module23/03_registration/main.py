def mail_check(mail):
    if '@' and '.' not in mail:
        return False
    else:
        return True


with open('registrations_good.log', 'w', encoding='utf-8') as reg_good, open('registrations_bad.log', 'w', encoding='utf-8') as reg_bad, open('registrations.txt', 'r', encoding='utf-8') as registrations:
    for i_line in registrations:
        try:
            clear_line = i_line.rstrip()
            people_list = clear_line.split()
            if len(people_list) != 3:
                reg_bad.write(clear_line)
                raise IndexError
            elif not people_list[0].isalpha():
                reg_bad.write(clear_line)
                raise NameError
            elif not mail_check(people_list[1]):
                reg_bad.write(clear_line)
                raise SyntaxError
            elif not 10 <= int(people_list[2]) <= 99:
                reg_bad.write(clear_line)
                raise ValueError
            else:
                reg_good.write(clear_line + '\n')
        except IndexError:
            reg_bad.write(' - НЕ присутствуют все три поля\n')
        except NameError:
            reg_bad.write(' - Поле "Имя" содержит НЕ только буквы\n')
        except SyntaxError:
            reg_bad.write(' - Поле "Имейл" НЕ содержит @ и . (точку)\n')
        except ValueError:
            reg_bad.write(' - Поле "Возраст" НЕ является числом от 10 до 99\n')
