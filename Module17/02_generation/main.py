from random import randint

length = int(input('Введите длину списка: '))
List = [randint(1, 100) for _ in range(length)]
List = [(1 if i_list % 2 == 0 else List[i_list] % 5) for i_list in range(len(List))]
print('Результат:', List)