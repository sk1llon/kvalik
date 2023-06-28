from random import randint

n = int(input('Введите кол-во чисел: '))
List = [randint(0, 100) for _ in range(n)]
print(List)
b = randint(0, n)
print(b)
a = randint(0, b)
print(a)
print(List[:a], List[b:])
