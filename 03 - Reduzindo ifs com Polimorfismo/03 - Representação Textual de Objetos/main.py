from movie import Movie
from series import Series


def main():
    movie = Movie("avengers, infinity war", 2020, 180)
    series = Series("atlanta", 2078, 6)

    series.get_like()
    series.get_like()

    programs = [movie, series]

    for program in programs:
        print(program)


if __name__ == '__main__':
    main()
