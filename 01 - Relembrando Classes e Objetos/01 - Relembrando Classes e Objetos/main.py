from movie import Movie
from series import Series


def main():
    movie = Movie("Movie", 2020, 180)
    print(f"Name: {movie.name}, Year: {movie.year}, Duration: {movie.duration}")

    series = Series("Series", 2078, 6)
    print(f"Name: {series.name}, Year: {series.year}, Seasons: {series.seasons}")


if __name__ == '__main__':
    main()
