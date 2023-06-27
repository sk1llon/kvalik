amount_of_numbers = int(input('Кол-во чисел: '))
numbers = []
reverse_numbers = []
for i in range(amount_of_numbers):
    print(i + 1, 'число', end=' ')
    number = int(input())
    numbers.append(number)
print('Последовательность:', numbers)
for index in range(len(numbers) - 1, -1, -1):
    reverse_numbers.append(numbers[index])
while True:
    if numbers[len(numbers) - 1] == reverse_numbers[0]:
        reverse_numbers.remove(reverse_numbers[0])
    else:
        break
print('Нужно приписать чисеЛ:', len(reverse_numbers))
print('Сами числа:', reverse_numbers)
