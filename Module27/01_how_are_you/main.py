from typing import Callable
import functools


def how_are_you(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Callable:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию ')
        return func(*args, **kwargs)
    return wrapped_func


@how_are_you
def test():
    for i in range(10):
        print(i)


@how_are_you
def test_2():
    for i in range(1, 100, 10):
        print(i)


test()
test_2()
