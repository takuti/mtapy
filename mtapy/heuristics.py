from .base import AttributionBase


class LastTouch(AttributionBase):

    def run(self, conversions, normalize=True):
        self.attribution = {c: 0. for c in self.channels}

        for path, value in conversions:
            self.attribution[path[-1]] += value

        if normalize:
            self.normalize()


class FirstTouch(AttributionBase):

    def run(self, conversions, normalize=True):
        self.attribution = {c: 0. for c in self.channels}

        for path, value in conversions:
            self.attribution[path[0]] += value

        if normalize:
            self.normalize()


class Linear(AttributionBase):

    def run(self, conversions, normalize=True):
        self.attribution = {c: 0. for c in self.channels}

        for path, value in conversions:
            n = len(path)
            for c in path:
                self.attribution[c] += value / n

        if normalize:
            self.normalize()


class Ushape(AttributionBase):

    def run(self, conversions, normalize=True):
        self.attribution = {c: 0. for c in self.channels}

        for path, value in conversions:
            edge_weight = 0.4 if len(path) > 2 else 0.5

            self.attribution[path[0]] += value * edge_weight
            self.attribution[path[-1]] += value * edge_weight
            n_intermediate = len(path) - 2
            for i in range(1, len(path) - 1):
                self.attribution[path[i]] += value * 0.2 / n_intermediate

        if normalize:
            self.normalize()


class TimeDecay(AttributionBase):

    def run(self, conversions, normalize=True):
        self.attribution = {c: 0. for c in self.channels}

        for path, value in conversions:
            ordered_unique_exposure = dict.fromkeys(path)

            base = 1 / sum(range(1, len(ordered_unique_exposure) + 1))
            for i, c in enumerate(ordered_unique_exposure, 1):
                self.attribution[c] += i * base * value

        if normalize:
            self.normalize()
