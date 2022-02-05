class Playlist(list):
    def __init__(self, name, programs):
        self.name = name
        self.__programs = programs

    @property
    def programs(self):
        return self.__programs

    # The "__len__" is a python data model, which allows for example (in this case) to use the "len()" function for the
    # object itself
    def __len__(self):
        return len(self.__programs)

    def __getitem__(self, item):
        return self.__programs[item]
