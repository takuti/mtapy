from unittest import TestCase

from mtapy.shapley import Shapley


class ShapleyTestCase(TestCase):

    def test(self):
        model = Shapley(['a', 'b', 'c'])
        conversions = [(('a',), 2), (('b', 'c',), 1), (('c', 'a', 'b',), 5)]

        model.run(conversions)
        expected = {'a': 0.409091, 'b': 0.295455, 'c': 0.295455}
        for k, v in model.attribution.items():
            self.assertAlmostEqual(expected[k], v, places=5)

        model.run(conversions, normalize=False)
        expected = {
            'a': 2.9999999999999996,
            'b': 2.1666666666666665,
            'c': 2.1666666666666665
        }
        for k, v in model.attribution.items():
            self.assertAlmostEqual(expected[k], v, places=5)
