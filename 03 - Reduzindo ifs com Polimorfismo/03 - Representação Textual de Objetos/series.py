from program import Program


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    # The "Dunder Methods" replace the default action of some native functions of Python, for example, the "str()"
    # with "__str__"
    def __str__(self):
        return f"Name: {self._name}, Year: {self.year}, Seasons: {self.seasons}, Likes: {self._likes}"
