from program import Program


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f"Name: {self._name}, Year: {self.year}, Seasons: {self.seasons}, Likes: {self._likes}"
