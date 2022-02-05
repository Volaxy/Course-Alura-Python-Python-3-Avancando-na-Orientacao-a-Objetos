class Program:
    def __init__(self, name, year):
        self._name = name
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    @property
    def likes(self):
        return self._likes

    def get_like(self):
        self._likes += 1

    def __str__(self):
        return f"Name: {self._name}, Year: {self.year}, Likes: {self._likes}"
