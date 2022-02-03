from movie import Movie
from series import Series


def main():
    movie = Movie("movie one", 2020, 180)
    series = Series("series one", 2020, 2)

    series.get_like()
    series.get_like()

    programs = [movie, series]

    for program in programs:
        program.print()


if __name__ == '__main__':
    main()
