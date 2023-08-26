from typing import Callable


def how_are_you(func: Callable) -> Callable:
    input('Как дела? ')
    print('А у меня не очень! Ладно, держи свою функцию ')
    return func


@how_are_you
def test():
    for i in range(10):
        print(i)


test()
