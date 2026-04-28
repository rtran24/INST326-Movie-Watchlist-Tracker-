# movie.py

class Movie:
    def __init__(self, title, year, genre, runtime):
        self.title = title
        self.year = year
        self.genre = genre
        self.runtime = runtime
        self.watched = False
        self.rating = None
        self.date_watched = None
    
    def mark_as_watched(self, rating, date):
        if not (1 <= rating <= 10):
            raise ValueError("Rating must be between 1 and 10")
        
        self.watched = True
        self.rating = rating
        self.date_watched = date
    
    def edit_details(self, title, year, genre, runtime):
        self.title = title
        self.year = year
        self.genre = genre
        self.runtime = runtime
    
    def to_dict(self):
        return {
            'title': self.title,
            'year': self.year,
            'genre': self.genre,
            'runtime': self.runtime,
            'watched': self.watched,
            'rating': self.rating,
            'date_watched': self.date_watched
        }