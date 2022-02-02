from program import Program


class Series(Program):
    def __init__(self, name, year, seasons):
        self._name = name
        self.year = year
        self.seasons = seasons
        self._likes = 0
