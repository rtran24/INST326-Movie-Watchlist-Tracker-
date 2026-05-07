# movie_watchlist_tracker.py

from movie import Movie, Watchlist
from statistics_function import show_statistics
from file_io import save_to_file, load_from_file

def main():
    watchlist = Watchlist()
    load_from_file(watchlist)
    
    while True:
        print("\nMovie Watchlist Tracker")
        print("1. Add Movie")
        print("2. Remove Movie")
        print("3. Mark movie as watched")
        print("4. Show all movies")
        print("5. Show watched movies")
        print("6. Show unwatched movies")
        print("7. Show Statistics")
        print("8. Edit Movie Details")
        print("9. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Enter movie title: ")
            year = input("Enter year: ")
            genre = input("Enter genre: ")
            runtime = int(input("Enter runtime in minutes: "))
            movie = Movie(title, year, genre, runtime)
            watchlist.add_movie(movie)
            print("Movie added.")
            save_to_file(watchlist)
        
        elif choice == "2":
            title = input("Enter movie title to remove: ")
            if watchlist.remove_movie(title):
                print("Movie removed")
                save_to_file(watchlist)
            else:
                print("Movie not found")
        
        elif choice == "3":
            title = input("Enter movie title: ")
            movie = watchlist.find_movie(title)
            if movie:
                rating = int(input("Enter rating from 1 to 10: "))
                date = input("Enter date watched (YYYY-MM): ")
                movie.mark_as_watched(rating, date)
                print("Movie marked as watched.")
                save_to_file(watchlist)
            else:
                print("Movie not found")
        
        elif choice == "4":
            print("\nAll Movies:")
            watchlist.show_all_movies()
        
        elif choice == "5":
            print("\nWatched Movies:")
            watchlist.show_watched_movies()
        
        elif choice == "6":
            print("\nUnwatched Movies:")
            watchlist.show_unwatched_movies()
        
        elif choice == "7":
            print("\n=== Statistics ===")
            show_statistics(watchlist)
        
        elif choice == "8":
            title = input("Enter movie title to edit: ")
            movie = watchlist.find_movie(title)
            if movie:
                print(f"Current: {movie.title}")
                new_title = input(f"New title ({movie.title}): ")
                if new_title:
                    movie.title = new_title
                new_year = input(f"New year ({movie.year}): ")
                if new_year:
                    movie.year = new_year
                new_genre = input(f"New genre ({movie.genre}): ")
                if new_genre:
                    movie.genre = new_genre
                new_runtime = input(f"New runtime ({movie.runtime}): ")
                if new_runtime:
                    movie.runtime = int(new_runtime)
                print("Movie updated.")
                save_to_file(watchlist)
            else:
                print("Movie not found")
        
        elif choice == "9":
            save_to_file(watchlist)
            print("Goodbye!")
            break
        
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()