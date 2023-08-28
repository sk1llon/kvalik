import functools
from typing import Callable, Any


def counter(func: Callable) -> Any:
    """
    Декоратор. Ведёт подсчёт вызовов декорируемой функции
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        print('Функция была вызвана {count} раз(а)'.format(count=wrapped_func.count))
        return func(*args, **kwargs)
    wrapped_func.count = 0
    return wrapped_func


@counter
def say_hello():
    """
    Декорируемая функция. Пишет приветствие
    """
    print('Привет!')


say_hello()
say_hello()
say_hello()
