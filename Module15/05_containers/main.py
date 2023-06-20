containers = []
n = int(input('Введите кол-во контейнеров: '))
index = 0
for _ in range(n):
    container = int(input('Введите вес контейнера: '))
    if container >= 200:
        while container >= 200:
            container = int(input('Ошибка! Вес контейнера не должен превышать 200 кг. Попробуйте ещё раз: '))
    containers.append(container)
new_container = int(input('Введите вес нового контейнера: '))
while index < len(containers) and containers[index] >= new_container:
    index += 1
print('Номер, который получит новый контейнер:',index+1)