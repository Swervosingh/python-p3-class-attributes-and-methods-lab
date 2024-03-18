class Song:
   
    count = 0 # keeps track of the total number of songs created.
   
    genres = [] # is a list that stores unique genres of all songs.
    
    artists = [] # is a list that stores unique artists of all songs.
   
    genre_count = {} # is a dictionary that counts how many songs belong to each genre.
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
    def add_to_count(self):
        Song.count += 1
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1





