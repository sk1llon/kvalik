import random


class Person:

    def __init__(self, name, satiety=50, money=0, food=50, days_completed_count=0):
        self.name = name
        self.satiety = satiety
        self.money = money
        self.food = food
        self.count = days_completed_count

    def check_info(self):
        dice = random.randint(1, 6)
        if self.satiety <= 0:
            raise ValueError
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif self.satiety < 20:
            self.eat()
        elif self.food < 10:
            self.market()
        elif self.money < 50:
            self.work()
        elif dice == 3 or 4 or 5 or 6:
            self.games()

    def eat(self):
        print('Сытость: ' + str(self.satiety), 'Еда: ' + str(self.food), sep='\n')
        self.satiety += 30
        self.food -= 30
        print(self.name, 'поел')
        print('Сытость: ' + str(self.satiety), 'Еда: ' + str(self.food), sep='\n')
        print()

    def work(self):
        print('Сытость: ' + str(self.satiety), 'Деньги: ' + str(self.money), sep='\n')
        self.satiety -= 10
        self.money += 20
        print(self.name, 'поработал')
        print('Сытость: ' + str(self.satiety), 'Деньги: ' + str(self.money), sep='\n')
        print()

    def games(self):
        print('Сытость: ' + str(self.satiety))
        self.satiety -= 10
        print(self.name, 'поиграл')
        print('Сытость: ' + str(self.satiety))
        print()

    def market(self):
        print('Еда: ' + str(self.food), 'Деньги: ' + str(self.money), sep='\n')
        self.food += 80
        self.money -= 30
        print(self.name, 'сходил в магазин')
        print('Еда: ' + str(self.food), 'Деньги: ' + str(self.money), sep='\n')
        print()


count = 0
person_1 = Person('Олег')
person_2 = Person('Дима')
while count < 31:
    try:
        person_1.check_info()
        person_2.check_info()
        person_1.count += 1
        person_2.count += 1
    except ValueError:
        print('К сожалению один или оба проживающих погибли...')
        break
    count += 1
if person_1.count == count and person_2.count == count:
    print('Вы успешно прожили!')
