def film_existence(movie, film_list):
    for i_film in film_list:
        if i_film == movie:
            return True
    return False

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favourite = []
n = int(input('Сколько фильмов хотите добавить? '))
for _ in range(n):
    film = input('Введите название фильма: ')
    if film_existence(film,films):
        favourite.append(film)
    else:
        print('Ошибка! Такого фильма нет')
print('Список любимых фильмов:',favourite)