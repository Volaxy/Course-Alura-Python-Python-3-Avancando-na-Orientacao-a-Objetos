class Series:
    def __init__(self, name, year, seasons):
        self.name = name
        self.year = year
        self.seasons = seasons
        self.likes = 0

    def get_like(self):
        self.likes += 1
