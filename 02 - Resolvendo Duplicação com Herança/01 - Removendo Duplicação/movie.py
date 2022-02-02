from program import Program


# The inheritance in the Pythons is represented for the "(MOTHER_CLASS_NAME)", inheriting features from the parent class
class Movie(Program):
    def __init__(self, name, year, duration):
        self._name = name.title()
        self.year = year
        self.duration = duration
        self._likes = 0
