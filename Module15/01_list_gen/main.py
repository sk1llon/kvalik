list = []
n = int(input('Введите число: '))
for a in range(1,n+1):
    if a % 2 == 1:
        list.append(a)
print(list)