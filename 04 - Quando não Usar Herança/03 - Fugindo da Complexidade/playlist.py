class Playlist(list):
    def __init__(self, name, programs):
        self.name = name
        self.__programs = programs

    @property
    def programs(self):
        return self.__programs

    @property
    def listing(self):
        return len(self.__programs)
