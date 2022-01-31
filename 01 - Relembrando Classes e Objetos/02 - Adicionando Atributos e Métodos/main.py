from movie import Movie
from series import Series


def main():
    movie = Movie("movie one", 2020, 180)
    print(movie.name)

    print(movie.likes)
    movie.get_like()
    movie.get_like()
    print(movie.likes)


if __name__ == '__main__':
    main()
