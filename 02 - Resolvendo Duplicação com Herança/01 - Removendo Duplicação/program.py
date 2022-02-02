class Program:
    def __init__(self, name, year):
        # Private attributes are not inherited to the child class. Ex.: self.__name = name
        # The convention is to use only one "_", to say that the variable is protected, not using "name mangling".
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
        self.likes += 1
