import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.my_song = Song("It's My Life", "Bon Jovi", "Crush", "4:28")

    def test_init(self):
        self.assertTrue(isinstance(self.my_song, Song))

    def test_str(self):
        my_life = "Bon Jovi - It's My Life from Crush - 4:28"
        self.assertEqual(str(self.my_song), my_life)

    def test_eq(self):
        self.other_song = Song("It's My Life", "Bon Jovi", "Crush", "4:28")
        self.assertTrue(self.other_song == self.my_song)

    def test_hash(self):
        self.assertIsNotNone(self.my_song)

    def test_get_length(self):
        self.assertEqual(self.my_song.get_length(), "4:28")

    def test_get_length(self):
        self.assertEqual(self.my_song.get_length(seconds), ['4', '28'])

if __name__ == '__main__':
    unittest.main()
