from unittest import TestCase

from mtapy.base import AttributionBase


class AttributionBaseTestCase(TestCase):

    def test(self):
        model = AttributionBase(['a', 'b', 'c'])
        conversions = [(('a',), 2), (('b', 'c',), 1), (('c', 'a', 'b',), 5)]

        model.run(conversions)
        self.assertEqual(model.attribution, {'a': 0., 'b': 0., 'c': 0.})

        model.run(conversions, normalize=False)
        self.assertEqual(model.attribution, {'a': 0., 'b': 0., 'c': 0.})
