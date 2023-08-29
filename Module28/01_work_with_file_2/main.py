class File:
    """
    Контекст-менеджер. Считывает или дозаписывает информацию в файл
    """
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None
        print('Начинаю работу с файлом')

    def __enter__(self):
        """
        Магический метод, который проверяет файл на наличие. В ином случае открывает такой же файл
        в режиме записи
        :return:
        """
        try:
            self.file = open(self.file_name, self.mode, encoding='utf-8')
        except FileNotFoundError:
            self.file = open(self.file_name, 'w', encoding='utf-8')
        finally:
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Магический метод, который закрывает файл
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.file.close()
        print('Работа с файлом {file} окончена'.format(
            file=self.file_name
        ))
        return True


with File('example.txt', 'r') as file:
    file.write('Победа')
