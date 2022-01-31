from movie import Movie
from series import Series


def main():
    movie = Movie("Movie", 2020, 180)
    print(movie)

    series = Series("Series", 2078, 6)
    print(series)


if __name__ == '__main__':
    main()
