from program import Program


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f"Name: {self._name}, Year: {self.year}, Duration: {self.duration}, Likes: {self._likes}"
