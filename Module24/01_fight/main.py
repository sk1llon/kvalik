import random


class Warriors:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def hit(self, target):
        target.health -= 20


warriors = [Warriors('Воин 1'), Warriors('Воин 2')]
while True:
    random_attacker = random.randint(0, 1)
    attacker, victim = warriors[random_attacker], warriors[random_attacker - 1]
    attacker.hit(victim)
    print(attacker.name, 'атакует', victim.name)
    print('У', victim.name, 'осталось', victim.health, 'здоровья')
    if victim.health <= 0:
        print(attacker.name, 'победил!')
        break
