import random


class Parents:

    def __init__(self, name, age, children, children_count):
        self.name = name
        self.age = age
        self.children = []
        self.children_count = 0

    def print_info(self):
        print('Name: ' + self.name, 'Age: ' + str(self.age), 'Children amount: ' + str(self.children_count), sep='\n')
        print()

    def calm_down(self, child):
        if child.calm_state == 1:
            print('Родители спешат утешить ребёнка')
            child.calm_state = 0
        else:
            print('Ребёнок спокоен')

    def feed(self, child):
        if child.hungry_state == 1:
            print('Родители спешат накормить ребёнка')
            child.hungry_state = 0
        else:
            print('Ребёнок сыт')


class Children:
    calm_states = {0: 'Спокоен', 1: 'Плачет'}
    hungry_states = {0: 'Сыт', 1: 'Голоден'}

    def __init__(self, name, age):
        self.name = name
        self.age = age


parent_1_name = input('Как зовут родителя? ')
parent_1_age = int(input('Сколько лет родителю? '))
parent_1 = Parents(parent_1_name, parent_1_age, children=[], children_count=0)

child_1_name = input('Как зовут ребёнка? ')
child_1_age = int(input('Сколько лет ребёнку? '))
child_1 = Children(child_1_name, child_1_age)
parent_1.children.append(child_1)
parent_1.children_count += 1

child_2_name = input('Как зовут ребёнка? ')
child_2_age = int(input('Сколько лет ребёнку? '))
child_2 = Children(child_1_name, child_1_age)
parent_1.children.append(child_1)
parent_1.children_count += 1
parent_1.print_info()

for i_child in parent_1.children:
    i_child.calm_state = random.randint(0, 1)
    i_child.hungry_state = random.randint(0, 1)
    parent_1.calm_down(i_child)
    parent_1.feed(i_child)

