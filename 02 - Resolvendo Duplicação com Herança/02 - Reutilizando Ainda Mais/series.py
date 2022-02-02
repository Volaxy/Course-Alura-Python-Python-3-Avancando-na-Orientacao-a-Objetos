from program import Program


class Series(Program):
    def __init__(self, name, year, seasons):
        # The "super" calls the mother class and then access the methods of her through to the "."
        super().__init__(name, year)
        self.seasons = seasons
