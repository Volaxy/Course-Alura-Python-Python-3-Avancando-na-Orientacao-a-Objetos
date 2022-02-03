class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self.programs = programs

    def total_programs(self):
        return len(self.programs)
