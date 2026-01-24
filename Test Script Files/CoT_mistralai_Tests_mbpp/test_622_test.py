import unittest
from mbpp_622_code import Iterable
from six.moves import range

class TestGetMedian(unittest.TestCase):

    def test_valid_inputs(self):
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 4), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 5), 3.5)
        self.assertEqual(get_median([], [], 0), None)
        self.assertEqual(get_median([1], [], 1), 1)
        self.assertEqual(get_median([1], [2], 1), 1.5)
        self.assertEqual(get_median([1, 3], [2, 4], 2), 2.5)
        self.assertEqual(get_median([1, 3], [2, 4], 3), 2.5)
        self.assertEqual(get_median([1, 3], [2, 4], 4), 2.5)

    def test_edge_cases(self):
        self.assertEqual(get_median([1, 3], [2], 1), 2)
        self.assertEqual(get_median([1, 3], [2], 2), 2)
        self.assertEqual(get_median([1, 3], [2], 3), 2)
        self.assertEqual(get_median([1, 3], [2], 4), 2)
        self.assertEqual(get_median([], [2], 1), None)
        self.assertEqual(get_median([1], [], 1), 1)
        self.assertEqual(get_median([1], [], 2), 1)
        self.assertEqual(get_median([1], [], 3), 1)
        self.assertEqual(get_median([], [2], 1), None)
        self.assertEqual(get_median([], [2], 2), None)
        self.assertEqual(get_median([], [2], 3), None)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, get_median, 1, 2, 3)
        self.assertRaises(TypeError, get_median, [1], 'str', 3)
        self.assertRaises(TypeError, get_median, [1], 2, 'str')
        self.assertRaises(TypeError, get_median, [1, 2], [3, 4], -1)
        self.assertRaises(TypeError, get_median, [1, 2], [3, 4], 0)
        self.assertRaises(TypeError, get_median, [1, 2], [3, 4], -2)
