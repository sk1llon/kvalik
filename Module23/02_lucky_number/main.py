import random

number = 0
sum_of_nums = 0
with open('out_file.txt', 'w') as out_file:
    try:
        while sum_of_nums < 777:
            number = int(input('Введите число: '))
            random_number = random.randint(1, 13)
            print(random_number)
            if random_number == 1:
                raise ValueError
            else:
                out_file.write(str(number) + '\n')
                sum_of_nums += number
    except ValueError:
        print('Вас постигла неудача!')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    finally:
        new_out_file = open('out_file.txt', 'r')
        new_out_file.read()
        new_out_file.close()
