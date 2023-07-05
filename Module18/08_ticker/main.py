first_string = input('Введите первую строку: ')
second_string = input('Введите вторую строку: ')
step = 1
test = False
while step <= len(second_string):
    new_string = second_string[-step:] + second_string[:-step]
    step += 1
    if new_string == first_string:
        test = True
        break
if test:
    print('Первая строка получится из второй со сдвигом', step - 1)
else:
    print('Первую строку нельзя получить из второй')