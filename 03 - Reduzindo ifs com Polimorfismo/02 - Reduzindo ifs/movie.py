from program import Program


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def print(self):
        print(f"Name: {self._name}, Year: {self.year}, Duration: {self.duration}, Likes: {self._likes}")
