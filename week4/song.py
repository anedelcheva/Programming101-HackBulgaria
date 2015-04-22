class Song:

    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.__length_parts = [int(part) for part in length.split(":")]

    def __str__(self):
        return "{} - {} from {} - {}".\
            format(self.artist, self.title, self.album, self.length)

    def __eq__(self, other):
        eq_title = self.title == other.title
        eq_artist = self.artist == other.artist
        eq_album = self.album == other.album
        eq_length = self.length == other.length
        return eq_title and eq_length and eq_artist and eq_album

    def __hash__(self):
        return hash(self.__str__())

    def get_length(self):
        return self.length

    def get_length(self, hours=False, minutes=False, seconds=False):
        # [1, 33, 40]
        # [33, 40]
        # [0, 40]
        hours_part = 0
        minutes_part = 0
        seconds_part = 0
        n = len(self.__length_parts)

        if n == 3:
            hours_part = self.__length_parts[0]
            minutes_part = self.__length_parts[1]
            seconds_part = self.__length_parts[2]
        elif n == 2:
            minutes_part = self.__length_parts[0]
            seconds_part = self.__length_parts[1]

        if hours:
            return hours_part

        if minutes:
            return hours_part * 60 + minutes_part

        if seconds:
            return hours_part * 60 * 60 + minutes_part * 60 + seconds_part


my_life = Song("It's My Life", "Bon Jovi", "Crush", "4:28")
#print (my_life.get_length(seconds=True))
#print (my_life.get_length())
