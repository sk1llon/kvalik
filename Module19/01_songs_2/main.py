violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

amount_of_songs = int(input('Сколько песен выбрать? '))
duration = 0
for i_song in range(1, amount_of_songs + 1):
    song = input('Название {0}-й песни: '.format(i_song))
    if song in violator_songs:
        duration += violator_songs[song]
    else:
        print('Такой песни нет!')
print('Общее время звучания песен: {0} минуты'.format(round(duration, 2)))
