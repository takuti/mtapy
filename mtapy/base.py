class AttributionBase(object):
    """Base class of all attribution models.

    Parameters
    ----------
    channels : array-like of str
        All the possible channel names.
    """

    def __init__(self, channels):
        self.channels = channels
        self.attribution = {c: 0. for c in channels}

    def run(self, conversions, normalize=True):
        """Build an attribution model and calculate per-channel contribution.

        Parameters
        ----------
            conversions : array-like of (array-like, int or float))
                Observed pairs of conversion path and number of conversions.

            normalize : bool, default; True
                Normalize contribution scores across the channels.
        """
        if normalize:
            self.normalize()

    def normalize(self):
        """Normalize the contribution scores across the channels so that sum of
        the scores becomes 1.0.
        """
        s = sum(self.attribution.values())
        for c in self.channels:
            if s == 0. or (c not in self.attribution.keys()):
                self.attribution[c] = 0.
            else:
                self.attribution[c] /= s
