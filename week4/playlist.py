from song import Song
from group import group
import random


class SongNotThere(Exception):
    pass

class Playlist:

    def __init__(self, name="Code", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.playlist = []
        song_index = -1
        self.songs_not_played = self.playlist

    def add_song(self, song):
        if song not in self.playlist:
            self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
        else:
            raise SongNotThere

    def add_songs(self, songs):
        for song in songs:
            if song not in self.playlist:
                self.playlist.append(song)

    def total_length(self):
        hours = 0
        minutes = 0
        seconds = 0
        time_seconds = 0
        for song in self.playlist:
            time_seconds += song.get_length(seconds=True)
        hours = time_seconds // 3600
        minutes = (time_seconds % 3600) // 60
        seconds = (time_seconds % 3600) % 60
        return str(hours) + ":" + str(minutes) + ":" + str(seconds)

    def artists(self):
        list_of_artists = []
        for song in self.playlist:
            list_of_artists.append(song.artist)
        list_of_artists.sort()
        occurrences = [len(list) for list in group(list_of_artists)]
        #print (group(list_of_artists))
        #print (occurrences)
        artist_num_songs = {}
        for i in range(len(occurrences)):
            artist_num_songs[group(list_of_artists)[i][0]] = occurrences[i]
        return artist_num_songs

     def next_song(self):
        if self.repeat and self.song_index == len(self.playlist) - 1:
            self.song_index = 0
            return self.playlist[self.song_index]
        elif self.shuffle:
            self.song_index = random.choice(self.songs_not_played)
            self.songs_not_played.remove(self.song_index)
            return self.playlist[self.song_index]
        else:
            self.song_index += 1
            self.songs_not_played.remove(song_index)
            return self.playlist[self.song_index]



my_life = Song("It's My Life", "Bon Jovi", "Crush", "4:28")
always = Song("Always", "Bon Jovi", "Crush", "4:10")
vetrove = Song("Vetrove", "Lili Ivanova", "Unknown", "5:4:48")
follow = Song("I follow", "Lykke", "Unknown", "3:23")
my_playlist = Playlist("Code", repeat=False, shuffle=False)
my_playlist.add_songs([my_life, vetrove, follow, always])
#print (my_playlist.total_length())
#print (my_playlist.artists())
print (my_playlist.songs_not_played)
