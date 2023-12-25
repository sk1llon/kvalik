import re


text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
private_cars = re.findall(r'\w\d{3}\w{2}\d{2,4}', text)
print('Список номеров частных автомобилей:', private_cars)
taxi = re.findall(r'\w{2}\d{3}\d{2,3}', text)
print('Список номеров такси:', taxi)
