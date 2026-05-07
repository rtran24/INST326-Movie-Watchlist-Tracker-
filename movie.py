# movie.py

from statistics_function import show_statistics

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
    def __str__(self):
        if self.watched:
            return (f"{self.title} ({self.year}) - {self.genre}, {self.runtime} min | Watched | Rating: {self.rating}/10")
        else:
            return (f"{self.title} ({self.year}) - {self.genre}, {self.runtime} min | Not Watched")

class Watchlist:
    def __init__(self):
        self.movies = []
    def add_movie(self, movie):
        self.movies.append(movie)
    def remove_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                self.movies.remove(movie)
                return True
        return False
    def find_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None
    def show_all_movies(self):
        for movie in self.movies:
            print(movie)
    def show_watched_movies(self):
        found = False
        for movie in self.movies:
            if movie.watched:
                print(movie)
                found = True
        if not found:
            print("No watched movies.")
    def show_unwatched_movies(self):
        found = False
        for movie in self.movies:
            if not movie.watched:
                print(movie)
                found = True
        if not found:
            print("No unwatched movies.")