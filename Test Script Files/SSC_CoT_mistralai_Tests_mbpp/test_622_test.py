import unittest
from mbpp_622_code import Iterable

class TestGetMedian(unittest.TestCase):

    def test_normal(self):
        self.assertAlmostEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)
        self.assertAlmostEqual(get_median([1, 3, 5], [2, 4, 6], 4), 3.5)
        self.assertAlmostEqual(get_median([1, 3, 5], [2, 4, 6], 5), 3.5)

    def test_edge_and_boundary(self):
        self.assertAlmostEqual(get_median([], [], 0), -1)
        self.assertAlmostEqual(get_median([1], [], 1), 1)
        self.assertAlmostEqual(get_median([1], [2], 1), 1.5)
        self.assertAlmostEqual(get_median([1], [2], 0), -1)
        self.assertAlmostEqual(get_median([1, 2], [], 2), 1.5)
        self.assertAlmostEqual(get_median([], [2], 2), 2)
        self.assertAlmostEqual(get_median([1, 2], [1, 2], 1), 1.5)
        self.assertAlmostEqual(get_median([1, 2], [1, 2], 2), 1.5)
        self.assertAlmostEqual(get_median([1, 2], [1, 2], 3), 1.5)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, get_median, 'str', 'list', 1)
        self.assertRaises(TypeError, get_median, [1], 2.5, 1)
        self.assertRaises(TypeError, get_median, [1], [], 1)
        self.assertRaises(TypeError, get_median, [], [1], 1)
        self.assertRaises(ValueError, get_median, [1], [1], -1)
        self.assertRaises(ValueError, get_median, [1], [1], 0)
