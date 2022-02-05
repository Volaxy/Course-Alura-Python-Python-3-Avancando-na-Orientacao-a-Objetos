class Playlist(list):
    def __init__(self, name, programs):
        super().__init__(programs)
        self.name = name
