import unittest
from playlist import Playlist
from playlist import SongNotThere
from song import Song


class PlaylistTest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("It's My Life", "Bon Jovi", "Crush", "4:28")
        self.song2 = Song("Vetrove", "Lili Ivanova", "Unknown", "5:4:48")
        self.song3 = Song("I follow", "Lykke", "Unknown", "3:23")
        self.song4 = Song("Written in the stars", "Tinie Tempah",
                          "Unknown", "3:36")
        self.song5 = Song("Tsvetove", "Neli Petkova", "Unknown", "3:31")
        self.song6 = Song("Samo men", "Neli Petkova", "Unknown", "3:52")
        self.my_playlist = Playlist("MY SONG", True, True)
        self.songs = [self.song1, self.song2, self.song3, self.song4,
                      self.song5, self.song6]
        self.songs_playlist = Playlist("New songs", False, False)
        self.songs_playlist.add_songs(self.songs)

    def test_init(self):
        self.assertTrue(self.my_playlist, Playlist)

    def test_add_song(self):
        self.assertNotIn(self.song1, self.my_playlist.playlist)
        self.my_playlist.add_song(self.song1)
        self.assertIn(self.song1, self.my_playlist.playlist)

    def test_remove_song(self):
        self.assertIn(self.song1, self.songs_playlist.playlist)
        self.songs_playlist.remove_song(self.song1)
        self.assertNotIn(self.song1, self.songs_playlist.playlist)

    def test_add_songs(self):
        list_of_songs = [self.song1, self.song2, self.song3]
        self.my_playlist.add_songs(list_of_songs)
        for song in list_of_songs:
            self.assertIn(song, self.my_playlist.playlist)

    def test_total_length(self):
        duration = self.songs_playlist.total_length()
        self.assertEqual(duration, "5:23:38")

    def test_artists(self):
        result = {'Bon Jovi': 1, 'Lili Ivanova': 1, 'Lykke': 1,
                  'Tinie Tempah': 1, 'Neli Petkova': 2}
        self.assertEqual(self.songs_playlist.artists(), result)

if __name__ == '__main__':
    unittest.main()
