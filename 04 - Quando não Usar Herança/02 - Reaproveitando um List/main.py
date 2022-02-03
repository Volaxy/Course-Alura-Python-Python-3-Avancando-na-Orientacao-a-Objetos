from movie import Movie
from playlist import Playlist
from series import Series


def main():
    avengers = Movie('avengers - infinity war', 2018, 160)
    atlanta = Series('atlanta', 2018, 2)
    tmep = Movie('everybody in panic', 1999, 100)
    demolisher = Series('demolisher', 2016, 2)

    tmep.get_like()
    demolisher.get_like()

    programs = [avengers, atlanta, tmep, demolisher]
    playlist = Playlist("weekend playlist", programs)

    for program in playlist:
        print(program)

    print(f"Playlist Length: {len(playlist)}")
    print(f"It's present?: {avengers in playlist}")


if __name__ == '__main__':
    main()
