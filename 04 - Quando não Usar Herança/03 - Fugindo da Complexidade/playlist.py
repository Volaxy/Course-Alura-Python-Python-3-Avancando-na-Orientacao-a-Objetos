class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    @property
    def programs(self):
        return self._programs

    @property
    def length(self):
        return len(self._programs)
