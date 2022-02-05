from program import Program


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    # The "Dunder Methods" replace the default action of some native functions of Python, for example, the "str()"
    # with "__str__"
    def __str__(self):
        return f"Name: {self._name}, Year: {self.year}, Duration: {self.duration}, Likes: {self._likes}"
