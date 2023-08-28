import time
from typing import Callable
import functools


def time_sleep(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Callable:
        time.sleep(5)
        return func(*args, **kwargs)
    return wrapped_func


@time_sleep
def main_func():
    for i in range(10):
        print(i)


@time_sleep
def test_func():
    for i in range(0, 100, 10):
        print(i)


main_func()
test_func()
