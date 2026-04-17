# movie.py

from datetime import datetime
from typing import Optional

class Movie:
    """
    A class representing a movie in the watchlist.
    
    Attributes:
        title (str): Movie title
        year (int): Release year
        genre (str): Movie genre (e.g., "Action", "Comedy", "Drama")
        runtime (int): Runtime in minutes
        watched (bool): Whether the movie has been watched
        rating (Optional[int]): Rating from 1-10 (None if not rated)
        date_watched (Optional[str]): Date watched in YYYY-MM-DD format
    """
    
    def __init__(self, title: str, year: int, genre: str, runtime: int):
        """
        Initialize a new Movie instance.
        
        Args:
            title: Movie title
            year: Release year
            genre: Movie genre
            runtime: Runtime in minutes
        """
        self.title = title
        self.year = year
        self.genre = genre
        self.runtime = runtime
        self.watched = False
        self.rating = None
        self.date_watched = None
    
    def mark_as_watched(self, rating: int, date_watched: str = None) -> bool:
        """
        Mark the movie as watched with a rating and optional date.
        
        Args:
            rating: Rating from 1-10
            date_watched: Date watched in YYYY-MM-DD format. If None, uses today's date.
            
        Returns:
            bool: True if successful, False if rating is invalid
            
        Raises:
            ValueError: If rating is out of range (1-10)
        """
        if not self._validate_rating(rating):
            raise ValueError(f"Invalid rating: {rating}. Rating must be between 1 and 10.")
        
        self.watched = True
        self.rating = rating
        
        if date_watched is None:
            self.date_watched = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date_watched = date_watched
        
        return True
    
    def edit_movie(self, title: str = None, year: int = None, 
                   genre: str = None, runtime: int = None) -> None:
        """
        Edit movie attributes.
        
        Args:
            title: New title (None to keep current)
            year: New year (None to keep current)
            genre: New genre (None to keep current)
            runtime: New runtime (None to keep current)
        """
        if title is not None:
            self.title = title
        if year is not None:
            self.year = year
        if genre is not None:
            self.genre = genre
        if runtime is not None:
            self.runtime = runtime
    
    def reset_watched_status(self) -> None:
        """Reset the movie to unwatched status, clearing rating and date."""
        self.watched = False
        self.rating = None
        self.date_watched = None
    
    def get_info(self) -> dict:
        """
        Get movie information as a dictionary.
        
        Returns:
            dict: Dictionary containing all movie attributes
        """
        return {
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "runtime": self.runtime,
            "watched": self.watched,
            "rating": self.rating,
            "date_watched": self.date_watched
        }
    
    def display_summary(self) -> str:
        """
        Generate a readable summary of the movie.
        
        Returns:
            str: Formatted movie summary
        """
        status = "✓ Watched" if self.watched else "○ Unwatched"
        rating_str = f" | Rating: {self.rating}/10" if self.rating else ""
        date_str = f" | Watched: {self.date_watched}" if self.date_watched else ""
        
        return (f"{self.title} ({self.year}) - {self.genre} ({self.runtime} min) - "
                f"{status}{rating_str}{date_str}")
    
    def to_dict(self) -> dict:
        """
        Convert movie to dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary representation of the movie
        """
        return {
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "runtime": self.runtime,
            "watched": self.watched,
            "rating": self.rating,
            "date_watched": self.date_watched
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Movie':
        """
        Create a Movie instance from a dictionary (for JSON loading).
        
        Args:
            data: Dictionary containing movie data
            
        Returns:
            Movie: New Movie instance with data from dictionary
        """
        movie = cls(
            title=data["title"],
            year=data["year"],
            genre=data["genre"],
            runtime=data["runtime"]
        )
        movie.watched = data.get("watched", False)
        movie.rating = data.get("rating")
        movie.date_watched = data.get("date_watched")
        return movie
    
    def _validate_rating(self, rating: int) -> bool:
        """
        Validate that rating is between 1 and 10.
        
        Args:
            rating: Rating to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        return isinstance(rating, int) and 1 <= rating <= 10
    
    def __str__(self) -> str:
        """String representation of the movie."""
        return self.display_summary()
    
    def __eq__(self, other) -> bool:
        """Compare two movies by title and year."""
        if not isinstance(other, Movie):
            return False
        return self.title.lower() == other.title.lower() and self.year == other.year