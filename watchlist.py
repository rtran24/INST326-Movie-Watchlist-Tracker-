# movie.py

from statistics_module import show_statistics

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
        found = False
        for movie in self.movies:
            if not movie.watched:
                print (movie)
                found = True
        if not found:
            return ("No unwatched movies.")

def main():
    watchlist = Watchlist()
    while True:
        print("Movie Watchlist Tracker")
        print("1. Add Movie")
        print("2. Remove Movie")
        print("3. Mark movie as watched")
        print("4. Show all movies")
        print("5. Show watched movies")
        print("6. Show unwatched movies")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Enter movie title: ")
            year = input("Enter year: ")
            genre = input("Enter genre: ")
            runtime = int(input("Enter runtime in minutes: "))
            movie = Movie(title, year, genre, runtime)
            watchlist.add_movie(movie)
            print ("Movie added.")
        elif choice == "2":
            title = input("Enter movie title to remove: ")
            if watchlist.remove_movie(title):
                print("Movie removed")
            else:
                print("Movie not found")
        elif choice == "3":
            title = input("Enter movie title: ")
            movie = watchlist.find_movie(title)
            if movie:
                rating = int(input("Enter rating from 1 to 10: "))
                date = input("Enter date watched: ")
                movie.mark_as_watched(rating, date)
                print("Movie marked as watched.")
            else:
                print ("Movie not found")
        elif choice == "4":
            watchlist.show_all_movies()
        elif choice == "5":
            watchlist.show_watched_movies()
        elif choice == "6":
            watchlist.show_unwatched_movies()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()
