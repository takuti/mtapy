from unittest import TestCase

from mtapy.heuristics import LastTouch, FirstTouch, Linear, Ushape, TimeDecay


class LastTouchTestCase(TestCase):

    def test(self):
        model = LastTouch(['a', 'b', 'c'])
        conversions = [(('a',), 2), (('b', 'c',), 1), (('c', 'a', 'b',), 5)]

        model.run(conversions)
        self.assertEqual(model.attribution,
                         {'a': 0.25, 'b': 0.625, 'c': 0.125})

        model.run(conversions, normalize=False)
        self.assertEqual(model.attribution, {'a': 2., 'b': 5., 'c': 1.})


class FirstTouchTestCase(TestCase):

    def test(self):
        model = FirstTouch(['a', 'b', 'c'])
        conversions = [(('a',), 2), (('b', 'c',), 1), (('c', 'a', 'b',), 5)]

        model.run(conversions)
        self.assertEqual(model.attribution,
                         {'a': 0.25, 'b': 0.125, 'c': 0.625})

        model.run(conversions, normalize=False)
        self.assertEqual(model.attribution, {'a': 2., 'b': 1., 'c': 5.})


class LinearTestCase(TestCase):

    def test(self):
        model = Linear(['a', 'b', 'c'])
        conversions = [(('a',), 2), (('b', 'c',), 1), (('c', 'a', 'b',), 5)]

        expected = {'a': 2. + 5 / 3, 'b': .5 + 5 / 3, 'c': .5 + 5 / 3}

        model.run(conversions, normalize=False)
        self.assertEqual(model.attribution, expected)

        model.run(conversions)
        s = sum(expected.values())
        self.assertEqual(model.attribution,
                         {k: v / s for k, v in expected.items()})


class UshapeTestCase(TestCase):

    def test(self):
        model = Ushape(['a', 'b', 'c'])
        conversions = [(('a',), 2), (('b', 'c',), 1), (('c', 'a', 'b',), 5)]

        expected = {'a': 2. + 5 * .2, 'b': .5 + 5 * .4, 'c': .5 + 5 * .4}

        model.run(conversions, normalize=False)
        self.assertEqual(model.attribution, expected)

        model.run(conversions)
        s = sum(expected.values())
        self.assertEqual(model.attribution,
                         {k: v / s for k, v in expected.items()})


class TimeDecayTestCase(TestCase):

    def test(self):
        model = TimeDecay(['a', 'b', 'c'])
        conversions = [(('a',), 2), (('b', 'c',), 1), (('c', 'a', 'b',), 5)]

        expected = {'a': 2 + 2 / 6 * 5,
                    'b': 1 / 3 + 3 / 6 * 5,
                    'c': 2 / 3 + 1 / 6 * 5}

        model.run(conversions, normalize=False)
        self.assertEqual(model.attribution, expected)

        model.run(conversions)
        s = sum(expected.values())
        self.assertEqual(model.attribution,
                         {k: v / s for k, v in expected.items()})
