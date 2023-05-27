def main(number):
    smallest_divisor = 0
    for a in range(number,1,-1):
        if number % a == 0:
            smallest_divisor = a
    print('Наименьший делитель, отличный от единицы:',smallest_divisor)
number = int(input('Введите число: '))
main(number)