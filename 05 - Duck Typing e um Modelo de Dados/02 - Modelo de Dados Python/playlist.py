class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    # The "__len__" function is relative to the function "len()"
    def __len__(self):
        return len(self._programs)

    @property
    def programs(self):
        return self._programs
