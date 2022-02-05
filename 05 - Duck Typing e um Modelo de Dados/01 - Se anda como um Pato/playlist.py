class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    # The "__getitem__" method defines that a class is an iterable
    # The double "__" represents the "Duck Typing", in which it is said that it is not necessary to implement or extend
    # all the behavior of a class 2 so that class 1 "be" a class 2, just put the methods of class 2 so that class 1
    # behaves in the same way
    def __getitem__(self, item):
        return self._programs[item]

    @property
    def programs(self):
        return self._programs

    @property
    def length(self):
        return len(self._programs)
