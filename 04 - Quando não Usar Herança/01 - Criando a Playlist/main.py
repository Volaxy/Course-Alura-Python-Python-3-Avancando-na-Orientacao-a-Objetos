from movie import Movie
from playlist import Playlist
from series import Series


def main():
    avengers = Movie('avengers - infinity war', 2018, 160)
    atlanta = Series('atlanta', 2018, 2)
    tmep = Movie('everybody in panic', 1999, 100)
    demolisher = Series('demolisher', 2016, 2)

    programs = [avengers, atlanta, tmep, demolisher]

    playlist = Playlist("Weekend Playlist", programs)

    for program in playlist.programs:
        print(program)


if __name__ == '__main__':
    main()
