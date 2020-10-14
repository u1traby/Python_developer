# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)
all_3 = float(violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[8][1])
print("Три песни из списка звучат", round(all_3, 2), "минут")

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут
song_1 = violator_songs_dict.get('Sweetest Perfection')
song_2 = violator_songs_dict.get('Policy of Truth')
song_3 = violator_songs_dict.get('Blue Dress')
next_3 = float(song_1 + song_2 + song_3)
print("Три песни из словаря звучат", round(next_3, 2), "минут")
song_4 = violator_songs_dict.get('World in My Eyes')
song_5 = violator_songs_dict.get('Waiting for the Night')
song_6 = violator_songs_dict.get('Personal Jesus')
next_next = float(song_4 + song_5 + song_6)
print("А другие три песни из словаря звучат", round(next_next, 2), "минут")
