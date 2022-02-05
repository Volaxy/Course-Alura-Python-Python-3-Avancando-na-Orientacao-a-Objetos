from movie import Movie
from series import Series


def main():
    movie = Movie("avengers, infinity war", 2020, 180)
    series = Series("atlanta", 2078, 6)

    movie.get_like()
    movie.get_like()
    series.get_like()

    print(f"Name: {movie.name}, Year: {movie.year}, Duration: {movie.duration}, Likes: {movie.likes}")
    print(f"Name: {series.name}, Year: {series.year}, Seasons: {series.seasons}, Likes: {series.likes}")


if __name__ == '__main__':
    main()
