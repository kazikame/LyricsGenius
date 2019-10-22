import lyricsgenius

genius = lyricsgenius.Genius("")
# artist = genius.search_artist("Andy Shauf")
song = genius.search_song("Rap God", "Eminem")
print(song.lyrics)