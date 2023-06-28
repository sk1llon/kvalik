import random

team_1 = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
team_2 = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
winners = [(team_1[index] if team_1[index] > team_2[index] else team_2[index])
           for index in range(20)]
print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', winners)
