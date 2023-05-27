def main(number):
    sum = 0
    while number > 0:
        count = number
        count %= 10
        sum += count
        number //= 10
    print()
    print('Сумма цифр:',sum)
    return sum
def count(number):
    count = 0
    while number > 0:
        new_number = number
        new_number %= 10
        count += 1
        number //= 10
    print('Количество цифр в числе:',count)
    return count
number = int(input('Введите число: '))
dividend = main(number)
divider = count(number)
answer = dividend - divider
print('Разность суммы и количества цифр:',answer)

