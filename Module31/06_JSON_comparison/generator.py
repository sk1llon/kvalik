import json


with open('json_new.json', 'r') as file:
    new_data = json.load(file)

with open('json_old.json', 'r') as file:
    old_data = json.load(file)


def list_comparison(old_lst, new_lst):
    dictionary_old = dict()
    dictionary_new = dict()
    for dct in old_lst:
        for keys, values in dct.items():
            dictionary_old[keys] = values
    for dct in new_lst:
        for keys, values in dct.items():
            dictionary_new[keys] = values
    json_comparison(dictionary_old, dictionary_new)


def json_comparison(old, new):
    for key in old.keys():
        if isinstance(old[key], dict):
            json_comparison(old[key], new[key])
        elif isinstance(old[key], list):
            list_comparison(old[key], new[key])
        elif old[key] != new[key]:
            yield 'Было:\n{key}: {old_value}\nСтало:\n{key}: {new_value}'\
                .format(key=key, old_value=old[key], new_value=new[key])


result = json_comparison(old_data, new_data)
for value in result:
    print(value)
