site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search(struct, elem, dep=None):
    if depth == 1:
        if elem in struct:
            return struct[elem]
    else:
        for substructure in struct.values():
            if isinstance(substructure, dict):
                result = search(substructure, elem)
                if result:
                    break
        else:
            result = None
        return result


element = input('Введите искомый ключ: ')
depth_yes_or_no = input('Хотите ввести максимальную глубину? Y/N: ')
if depth_yes_or_no == 'Y':
    depth = int(input('Введите максимальную глубину '))
    print('Значение ключа:', search(site, element, depth))
elif depth_yes_or_no == 'N':
    print('Значение ключа:', search(site, element))
else:
    print('Ошибка!')
