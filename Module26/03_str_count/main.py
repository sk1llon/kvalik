import os
from collections.abc import Iterable


def generator(link: str) -> Iterable[tuple]:
    for links, dirs, files in os.walk(link):
        for file in files:
            count = 0
            if os.path.join(link, file).endswith('.py'):
                cur_file = open(os.path.join(link, file), 'r', encoding='utf-8')
                for i_str in cur_file.readlines():
                    if not (i_str == '\n' or i_str.strip().startswith(('"', '#', "'"))):
                        count += 1
                yield os.path.join(link, file), count


main_path = os.path.abspath(os.path.join('..', '01_num_squares'))
for i_elem in generator(link=main_path):
    print('Файл {link}, строк кода: {count}'.format(
        link=i_elem[0],
        count=i_elem[1]
        )
    )
