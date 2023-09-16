from typing import Callable, Optional
from functools import wraps


app = dict()


def callback(_func_name: Optional[Callable] = None, *, rt: str = None) -> Callable:
    def decorator(func_name):
        app[rt] = func_name

        @wraps(func_name)
        def wrapped_func(*args, **kwargs):
            result = func_name(*args, **kwargs)
            return result
        return wrapped_func
    if _func_name is None:
        return decorator
    return decorator(_func_name)


@callback(rt='11')
def example():
    print('Пример функции')
    return 'OK'


route = app.get('11')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
route = app.get('1')
if route:
    response = route()
    print('Ответ', response)
else:
    print('Такого пути нет')