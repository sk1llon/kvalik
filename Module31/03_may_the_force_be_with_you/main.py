import requests
import json

# не скачивается библиотека swapi, поэтому я сделаю через requests и json


link = 'https://swapi.dev/api/starships/10/'
my_req = requests.get(link)
data = json.loads(my_req.text)
print('Название корабля:', data.get('name'))
print('Максимальная скорость:', data.get('max_atmosphering_speed'))
print('Класс:', data.get('starship_class'))
pilot_list = data.get('pilots')
with open('my_file.json', 'a') as file:
    file.write('\nInformation about starship: \n')
    json.dump(data, file, indent=4)
for pilot_link in pilot_list:
    pilot_req = requests.get(pilot_link)
    pilot_data = json.loads(pilot_req.text)
    print('\nПилот {name}'.format(name=pilot_data.get('name')))
    print('Рост:', pilot_data.get('height'))
    print('Вес:', pilot_data.get('mass'))
    homeworld_request = requests.get(pilot_data.get('homeworld'))
    homeworld_data = json.loads(homeworld_request.text)
    print('Родная планета:', homeworld_data.get('name', None))
    print('Ссылка на информацию о родной планете:', pilot_data.get('homeworld'))
    with open('my_file.json', 'a') as file:
        file.write('\nInformation about pilot: \n')
        json.dump(pilot_data, file, indent=4)

