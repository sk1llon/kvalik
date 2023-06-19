names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []
index = 0
for index in range(8):
    if index % 2 == 0:
        first_day.append(names[index])
print(first_day)
