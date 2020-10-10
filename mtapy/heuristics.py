from .base import AttributionBase


class LastTouch(AttributionBase):

    def run(self, conversions, normalize=True):
        self.attribution = {c: 0. for c in self.channels}

        for path, value in conversions:
            self.attribution[path[-1]] += value

        if normalize:
            self.normalize()
