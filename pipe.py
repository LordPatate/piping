from collections.abc import Callable, Iterable
from typing import Any


class Pipe(Iterable):
    def __init__(self, iterable: Iterable | None = None):
        if iterable is None:
            iterable = []
        self._iterable = iterable

    def __iter__(self):
        return iter(self._iterable)

    def all(self, p: Callable[[Any], bool]):
        return all(p(x) for x in self._iterable)

    def any(self, p: Callable[[Any], bool]):
        return any(p(x) for x in self._iterable)

    def dict(self, **kwargs):
        return dict(self._iterable, **kwargs)

    def enumerate(self, **kwargs):
        self._iterable = enumerate(self._iterable, **kwargs)
        return self

    def filter(self, p: Callable[[Any], bool]):
        self._iterable = filter(p, self._iterable)
        return self

    def frozenset(self):
        return frozenset(self._iterable)

    def len(self):
        return len(self._iterable)

    def list(self):
        return list(self._iterable)

    def map(self, f: Callable):
        self._iterable = map(f, self._iterable)
        return self

    def max(self, **kwargs):
        return max(self._iterable, **kwargs)

    def min(self, **kwargs):
        return min(self._iterable, **kwargs)

    def next(self):
        return next(self._iterable)

    def reversed(self):
        self._iterable = reversed(list(self._iterable))
        return self

    def set(self):
        return set(self._iterable)

    def sorted(self, **kwargs):
        self._iterable = sorted(self._iterable, **kwargs)
        return self

    def sum(self, **kwargs):
        return sum(self._iterable, **kwargs)

    def tuple(self):
        return tuple(self._iterable)
