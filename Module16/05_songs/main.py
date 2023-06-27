violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

duration = 0
amount = int(input('Введите кол-во песен: '))
for _ in range(amount):
    track = input('Введите название трека: ')
    for i_song in range(len(violator_songs)):
        if track == violator_songs[i_song][0]:
            duration += violator_songs[i_song][1]
print('Общее время звучания песен в минутах:', round(duration, 2))
