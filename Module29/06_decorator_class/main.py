import time


class LoggerDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Вызов функции', self.func.__name__)
        start = time.time()
        my_res = self.func(*args, **kwargs)
        print('Аргументы: {arguments}\nРезультат: {result}\nВремя выполнения: {time}'.format(
            arguments=args,
            result=my_res,
            time=time.time() - start
        ))
        return my_res


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
