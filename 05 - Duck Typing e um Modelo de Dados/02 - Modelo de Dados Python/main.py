from movie import Movie
from playlist import Playlist
from series import Series


def main():
    avengers = Movie('avengers - infinity war', 2018, 160)
    atlanta = Series('atlanta', 2018, 2)
    tmep = Movie('everybody in panic', 1999, 100)
    demolisher = Series('demolisher', 2016, 2)
    demolisher2 = Series('demolisher 2', 2016, 2)

    tmep.get_like()
    demolisher.get_like()

    programs = [avengers, atlanta, tmep, demolisher]
    playlist = Playlist("weekend playlist", programs)

    for program in playlist.programs:
        print(program)

    print(f"\nPlaylist Length: {len(playlist)}", end="\n\n")

    print(f"Position 1: {playlist[0]}", end="\n\n")

    print(f"It's present?: {avengers in playlist}")
    print(f"It's present?: {demolisher2 in playlist}")


if __name__ == '__main__':
    main()
