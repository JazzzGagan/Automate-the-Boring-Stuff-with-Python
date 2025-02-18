def topsongs(albums, leftwidth, rightwidth):
    print('Top 10 Songs'.center(leftwidth + rightwidth, '-'))
    for k , v in albums.items():
          print(k.ljust(leftwidth, '.') + str(v).rjust(rightwidth))
listofsongs = {'pull me under': 1 , 'Nothing else matter': 2, 'day and age': 3, 'Neon': 4, 'i feel a part': 5}
topsongs(listofsongs, 12, 5)
topsongs(listofsongs, 20, 6)
