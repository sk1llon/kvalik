def main(begin,end):
    print(f'Годы от {begin} до {end} с тремя одинаковыми цифрами: ')
    for i in range(begin, end):
        if i % 10 == i // 10 % 10:
            if i % 10 == i // 1000 and not i % 10 == i // 100 % 10:
                print(i)
            elif not i % 10 == i // 1000 and i % 10 == i // 100 % 10:
                print(i)
            elif i // 1000 == i // 100 % 10:
                if i // 1000 == i % 10 and not i // 1000 == i // 10 % 10:
                    print(i)
            elif not i // 1000 == i % 10 and i // 1000 == i // 10 % 10:
                print(i)
beginning_of_interval = int(input("Введите начало интервала: "))
ending_of_interval = int(input("Введите конец интервала: "))
main(beginning_of_interval,ending_of_interval)