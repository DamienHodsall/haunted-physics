import mpv

"""
this didn't work for me
"""

player = mpv.MVP()

player.loadlist('images.txt')
player.playlist_shuffle()
