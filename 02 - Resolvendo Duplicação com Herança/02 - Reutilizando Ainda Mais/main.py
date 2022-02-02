from movie import Movie
from series import Series


def main():
    movie = Movie("movie one", 2020, 180)
    print(movie.name)
    movie.name = "the wonderfully chocolate fabric"
    print(movie.name)

    series = Series("movie one", 2020, 180)
    print(series.name)
    series.name = "cobra kai"
    print(series.name)


if __name__ == '__main__':
    main()
