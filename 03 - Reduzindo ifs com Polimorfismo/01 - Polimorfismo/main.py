from movie import Movie
from series import Series


def main():
    movie = Movie("avengers, infinity war", 2020, 180)
    series = Series("atlanta", 2078, 6)

    movie.get_like()
    movie.get_like()

    series.get_like()
    series.get_like()

    programs = [movie, series]

    for program in programs:
        # The "hasattr" verify if the object contains the attribute name in the second parameter
        details = program.duration if hasattr(program, "duration") else program.seasons

        print(f"Name: {program.name}, Details: {details}, Likes: {program.likes}")


if __name__ == '__main__':
    main()
