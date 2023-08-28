from datetime import datetime
from typing import Callable
import functools


def logging(func: Callable) -> Callable:
    """
    Декоратор. Отвечает за логирование функция
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Callable:
        print('Вызывается функция: {func_name}\t'
              'Позиционные аргументы: {args}\t'
              'Именованные аргументы: {kwargs}\t'.format(
                func_name=func.__name__,
                args=args,
                kwargs=kwargs
                ))
        result = func(*args, **kwargs)
        print('Функция завершила свою работу')
        return result
    return wrapped_func


@logging
def decorated_func():
    """
    Декорируемая функция. Делает отсчёт от 0 до 10
    :return:
    """
    try:
        for i in range(10):
            print(a)
    except Exception as exc:
        with open('function_errors.log', 'a', encoding='utf-8') as errors_log:
            errors_log.write('\nФункция: decorated_func\nОшибка: ' + str(type(exc)) + '\n' + 'Время ошибки: ' + str(datetime.now()))


@logging
def decorated_func_2():
    """
    Декорируемая функция. Делает отсчёт от 0 до 100 с шагом в 10
    :return:
    """
    try:
        for i in range(0, 100, 10):
            print(b)
    except Exception as exc:
        with open('function_errors.log', 'a', encoding='utf-8') as errors_log:
            errors_log.write(
                '\nФункция: decorated_func_2\nОшибка: ' + str(type(exc)) + '\n' + 'Время ошибки: ' + str(datetime.now())
                             )


decorated_func()
decorated_func_2()
