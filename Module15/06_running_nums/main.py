box = [1, 2, 3, 4, 5]
k = int(input('Сдвиг: '))
memory = 0
for i in range(k):
    memory = box[-1]
    box.insert(0,memory)
    box.pop(-1)
print(box)