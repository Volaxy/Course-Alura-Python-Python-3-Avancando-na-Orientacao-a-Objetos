from abc import ABC

from collections.abc import MutableSequence
from numbers import Complex


class Number(Complex):
    def __getitem__(self, item):
        super().__getitem__()


movies = Number()
