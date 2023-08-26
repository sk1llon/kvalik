from typing import Callable, Any
import functools


def cache_decorate(func: Callable) -> Any:
    """
    Декоратор. Выполняет кеширование чисел Фибоначчи
    :param func:
    :return:
    """
    cache = dict()

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        """
        Встроенная функция. Формирует словарь из чисел Фибоначчи
        :param args:
        :param kwargs:
        :return:
        """
        if args in cache:
            yield cache[args]
        else:
            result = func(*args, **kwargs)
            cache[args] = result
            yield result
        return wrapped_func


@cache_decorate
def fibonacci(number: int) -> int:
    """
    Декорируемая функция. Выполняет вычисление чисел Фибоначчи
    :param number:
    :return:
    """
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(5))
