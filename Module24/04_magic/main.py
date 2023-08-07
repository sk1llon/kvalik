class Earth:
    title = 'Земля'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()


class Fire:
    title = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()


class Air:
    title = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()


class Water:
    title = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            print(other)
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()


class Storm:
    title = 'Шторм'


class Steam:
    title = 'Пар'


class Dirt:
    title = 'Грязь'


class Lightning:
    title = 'Молния'


class Dust:
    title = 'Пыль'


class Lava:
    title = 'Лава'


first_element = Earth()
second_element = Fire()
result = first_element + second_element
print('{} + {} = {}'.format(
    first_element.title, second_element.title, result.title
))
