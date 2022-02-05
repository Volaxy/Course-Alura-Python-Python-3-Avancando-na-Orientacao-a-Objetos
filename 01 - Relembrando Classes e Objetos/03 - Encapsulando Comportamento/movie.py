class Movie:
    # In Python, you should set as private only what you want to protect, to avoid code complexity
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
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
