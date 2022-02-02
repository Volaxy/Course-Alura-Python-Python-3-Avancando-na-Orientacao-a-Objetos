from program import Program


class Movie(Program):
    def __init__(self, name, year, duration):
        # The "super" calls the mother class and then access the methods of her through to the "."
        super().__init__(name, year)
        self.duration = duration
