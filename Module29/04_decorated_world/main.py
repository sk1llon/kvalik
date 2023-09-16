from typing import Callable
from functools import wraps


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    @wraps(func)
    def wrapped_func(*func_args, **func_kwargs) -> Callable:
        print('Переданные арги и кварги в декоратор: {}'.format(args, kwargs))
        return func(*func_args, **func_kwargs)
    return wrapped_func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
