from typing import Callable, Any
from functools import wraps
import time


def log_methods(date_n_time: str) -> Callable:
    def log_decorator(cls):
        for method_name in dir(cls):
            if not method_name.startswith('__'):
                current_method = getattr(cls, method_name)
                decorated_method = timer(cls, current_method, date_n_time)
                setattr(cls, method_name, decorated_method)
        return cls
    return log_decorator


def timer(cls, func: Callable, date: str) -> Callable:
    @wraps(func)
    def wrapped_func(*args, **kwargs) -> Callable:
        start = time.time()
        print("Запускается '{cls_name}.{func_name}'. Дата и время запуска: {date_and_time}".format(
            cls_name=cls.__name__,
            func_name=func.__name__,
            date_and_time=date
        ))
        result = func(*args, **kwargs)
        print("Завершение '{cls_name}.{func_name}, время работы = {time}".format(
            cls_name=cls.__name__,
            func_name=func.__name__,
            time=time.time() - start
        ))
        return result
    return wrapped_func


@log_methods(date_n_time="Sep 16 2023 - 15:41:22")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods(date_n_time="Sep 17 2023 - 12:22:34")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
