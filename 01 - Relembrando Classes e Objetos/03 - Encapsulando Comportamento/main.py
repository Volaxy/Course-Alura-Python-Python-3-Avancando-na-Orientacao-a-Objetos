from movie import Movie
from series import Series


def main():
    # The private attributes and the methods of get and set prevent code from breaking when an attribute name changes
    movie = Movie("avengers, infinity war", 2020, 180)
    print(movie.name)
    movie.name = "the wonderfully chocolate fabric"
    print(movie.name)

    series = Series("atlanta", 2078, 6)
    print(series.name)
    series.name = "cobra kai"
    print(series.name)

    movie.get_like()
    movie.get_like()
    series.get_like()

    print(f"\nName: {movie.name}, Year: {movie.year}, Duration: {movie.duration}, Likes: {movie.likes}")
    print(f"Name: {series.name}, Year: {series.year}, Seasons: {series.seasons}, Likes: {series.likes}")


if __name__ == '__main__':
    main()
