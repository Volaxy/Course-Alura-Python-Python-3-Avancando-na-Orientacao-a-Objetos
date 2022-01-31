class Movie:
    def __init__(self, name, year, duration):
        self.name = name.title()
        self.year = year
        self.duration = duration
        self.likes = 0

    def get_like(self):
        self.likes += 1
