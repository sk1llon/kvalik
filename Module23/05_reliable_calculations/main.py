def get_sage_sqrt(num):
    try:
        if isinstance(num, int or float):
            try:
                if num >= 0:
                    return round(num ** 2, 3)
                else:
                    raise ValueError
            except ValueError:
                print('Число отрицательное!')
        else:
            raise TypeError
    except TypeError:
        print('Это не число!')


numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    if result != None:
        print(f"Квадратный корень numbers {number}: {result}")
