box = []
n = int(input('Введите кол-во чисел в списке: '))
for _ in range(n):
    digit = int(input('Введите число: '))
    box.append(digit)
k = int(input('Сдвиг: '))
memory = 0
for i in range(k):
    memory = box[-1]
    box.insert(0, memory)
    box.pop(-1)
print(box)