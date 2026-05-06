from collections import Counter

def get_average_rating(watchlist):
    watched = [m for m in watchlist.movies if m.watched and m.rating is not None]
    if not watched:
        return None
    return round(sum(m.rating for m in watched) / len(watched), 2)

def get_favorite_genre(watchlist):
    watched = [m for m in watchlist.movies if m.watched]
    if not watched:
        return None
    genre_counts = Counter(m.genre for m in watched)
    return genre_counts.most_common(1)[0][0]

def get_movies_per_month(watchlist):
    watched = [m for m in watchlist.movies if m.watched and m.date_watched]
    counts = Counter()
    for m in watched:
        month_key = m.date_watched[:7]
        counts[month_key] += 1
    return dict(sorted(counts.items()))

def get_total_watched(watchlist):
    return sum(1 for m in watchlist.movies if m.watched)

def get_total_runtime_watched(watchlist):
    return sum(m.runtime for m in watchlist.movies if m.watched)

def show_statistics(watchlist):
    """Prints a full statistics summary."""
    print(f"Total movies watched: {get_total_watched(watchlist)}")
    print(f"Total runtime watched: {get_total_runtime_watched(watchlist)} min")

    avg = get_average_rating(watchlist)
    print(f"Average rating: {avg}/10" if avg else "Average rating: N/A")

    genre = get_favorite_genre(watchlist)
    print(f"Favorite genre: {genre}" if genre else "Favorite genre: N/A")

    print("\nMovies watched per month:")
    per_month = get_movies_per_month(watchlist)
    if per_month:
        for month, count in per_month.items():
            print(f" {month}: {count} movie{'s' if count != 1 else ''}")
    else:
        print("  No data yet.")