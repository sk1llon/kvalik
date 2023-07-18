import copy


def sites_title(structure, name_key, name_value):
    if name_key in structure:
        structure[name_key] = name_value
        return site
    for substructure in structure.values():
        if isinstance(substructure, dict):
            result = sites_title(substructure, name_key, name_value)
            if result:
                return site


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {0} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {0}',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
amount_of_sites = int(input('Введите кол-во сайтов: '))
for _ in range(amount_of_sites):
    deep_copy = dict()
    site_result = dict()
    name_of_site = input('Введите название продукта для нового сайта: ')
    key = {'title': f'Куплю продам {name_of_site} недорого', 'h2': f'У нас самая низкая цена на {name_of_site}'}
    for i_key in key:
        sites_title(site, i_key, key[i_key])
    deep_copy = copy.deepcopy(site)
    head_name_of_site = 'Сайт для {}'.format(name_of_site)
    site_result[head_name_of_site] = deep_copy
    for key, value in site_result.items():
        print(key)
        print(value)

