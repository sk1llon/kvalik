from collections.abc import Iterable


class Sequence:
    def __init__(self, limit_num: int) -> None:
        self.limit_num = limit_num
        self.first_element = 0
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.count += 1
        if self.limit_num <= 0:
            raise StopIteration
        elif self.limit_num >= 1:
            if self.count > self.limit_num:
                raise StopIteration
            self.first_element += 1
        return self.first_element ** 2


def sequence(num: int) -> Iterable[int]:
    for i_num in range(1, num + 1):
        yield i_num ** 2


number = int(input('Введите число: '))
for i_elem in sequence(number):
    print(i_elem, end=' ')

print()

numbers = (i_elem ** 2 for i_elem in range(1, number + 1))
for i_element in numbers:
    print(i_element, end=' ')

print()

iterator = Sequence(number)
for i_el in iterator:
    print(i_el, end=' ')
