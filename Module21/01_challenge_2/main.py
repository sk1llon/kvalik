def sequence(num, i=1):
    print(i)
    if i != num:
        sequence(num, i+1)


sequence(int(input('Введите число: ')))
