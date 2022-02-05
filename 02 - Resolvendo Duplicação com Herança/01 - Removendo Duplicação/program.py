class Program:
    def __init__(self, name, year):
        # Private attributes are not inherited to the child class. Ex.: self.__name = name
        # The convention is to use only one "_", to say that the variable is protected, not using "name mangling".
        # when using 1 "_" instead of 2 "__", the use of "name mangling" is avoided, which is the transformation of the
        # name of the parent attribute, and preventing the same attribute from being passed on to the child classes
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
