import math


class MyMath:
    @classmethod
    def circle_len(cls, radius: int) -> float:
        """
        Метод для нахождения длины круга
        :param radius:
        :return:
        """
        return round(2 * math.pi * radius, 3)

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        """
        Метод для нахождения площади круга
        :param radius:
        :return:
        """
        return round(math.pi * radius ** 2, 3)

    @classmethod
    def square_vol(cls, side: int) -> int:
        """
        Метод для нахождения объёма куба
        :param side:
        :return:
        """
        return side ** 3

    @classmethod
    def sphere_sur(cls, radius: int) -> float:
        """
        Метод для нахождения площади поверхности сферы
        :param radius:
        :return:
        """
        return round(4 * math.pi * radius ** 2, 3)


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.square_vol(side=4)
res_4 = MyMath.sphere_sur(radius=4)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
