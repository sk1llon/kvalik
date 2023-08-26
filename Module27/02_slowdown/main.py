import time
from typing import Callable


def time_sleep(func: Callable) -> Callable:
    time.sleep(5)
    return func


@time_sleep
def main_func():
    for i in range(10):
        print(i)


main_func()
