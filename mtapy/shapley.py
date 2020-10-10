import numpy as np
from itertools import combinations

from .base import AttributionBase


class Shapley(AttributionBase):

    def run(self, conversions, normalize=True):
        self.attribution = {c: 0. for c in self.channels}

        S = {}
        for path, value in conversions:
            k = tuple(sorted(set(path)))
            if k not in S:
                S[k] = 0
            S[k] += value

        n = len(self.channels)
        n_factorial = np.math.factorial(n)

        for c in self.channels:
            for m in range(1, n + 1):
                for path in combinations(set(self.channels) - {c}, m):
                    s = len(path)
                    w = np.math.factorial(s)\
                        * np.math.factorial(n - s - 1) / n_factorial
                    self.attribution[c] += w\
                        * (self._v(S, path + (c,)) - self._v(S, path))

        if normalize:
            self.normalize()

    def _v(self, S, coalition):
        """
        total number of conversions generated by all subsets of the coalition;
        coalition is a tuple of channels
        """

        s = len(coalition)

        total_convs = 0

        for n in range(1, s + 1):
            for path in combinations(coalition, n):
                k = tuple(sorted(set(path)))
                if k in S:
                    total_convs += S[k]

        return total_convs