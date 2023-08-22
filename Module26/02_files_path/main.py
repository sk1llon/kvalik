import os
from collections.abc import Iterable


def gen_files_path(link: str, search: str) -> Iterable[str]:
    for links, dirs, files in list(os.walk(link)):
        for file in files:
            yield links + '\\' + file
            if links.split('\\')[-1] == search:
                return


main_path = os.path.abspath(os.path.join('..'))
result = gen_files_path(main_path, 'Python_Basic')
for i_path in result:
    print(i_path)
