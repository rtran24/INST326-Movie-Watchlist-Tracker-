# file_io.py

import json
from movie import Movie

def save_to_file(watchlist):
    data = []
    for movie in watchlist.movies:
        data.append(movie.to_dict())
    with open("watchlist_data.json", "w") as f:
        json.dump(data, f, indent=4)

def load_from_file(watchlist):
    try:
        with open("watchlist_data.json", "r") as f:
            data = json.load(f)
        for movie_data in data:
            movie = Movie(movie_data['title'], movie_data['year'], movie_data['genre'], movie_data['runtime'])
            if movie_data['watched']:
                movie.watched = True
                movie.rating = movie_data['rating']
                movie.date_watched = movie_data['date_watched']
            watchlist.add_movie(movie)
    except FileNotFoundError:
        pass