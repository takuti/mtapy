from unittest import TestCase

from mtapy.heuristics import LastTouch


class LastTouchTestCase(TestCase):

    def test(self):
        model = LastTouch(['a', 'b', 'c'])
        conversions = [(('a',), 2), (('b', 'c',), 1), (('c', 'a', 'b',), 5)]

        model.run(conversions)
        self.assertEqual(model.attribution,
                         {'a': 0.25, 'b': 0.625, 'c': 0.125})

        model.run(conversions, normalize=False)
        self.assertEqual(model.attribution, {'a': 2., 'b': 5., 'c': 1.})
