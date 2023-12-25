import json


with open('json_new.json', 'r') as file:
    new_data = json.load(file)

with open('json_old.json', 'r') as file:
    old_data = json.load(file)


def json_comparison(old, new):
    for key in old.keys():
        if isinstance(old[key], dict):
            json_comparison(old[key], new[key])
        elif old[key] != new[key]:
            old_diff[key] = old[key]
            new_diff[key] = new[key]


old_diff = dict()
new_diff = dict()
json_comparison(old_data, new_data)
print('Было:\n', old_diff, '\nСтало:\n', new_diff)
