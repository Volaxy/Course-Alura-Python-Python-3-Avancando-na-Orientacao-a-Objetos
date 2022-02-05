class Series:
    def __init__(self, name, year, seasons):
        self.__name = name
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()

    @property
    def likes(self):
        return self.__likes

    def get_like(self):
        self.__likes += 1
