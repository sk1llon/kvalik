from typing import List
from functools import reduce


def product(num_1, num_2):
    return num_1 * num_2


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

list_1 = list(map(lambda x: round(x**3, 3), floats))
print(list_1)
list_2 = list(filter(lambda x: len(x) > 5, names))
print(list_2)
reduce_3 = reduce(product, numbers)
print(reduce_3)
