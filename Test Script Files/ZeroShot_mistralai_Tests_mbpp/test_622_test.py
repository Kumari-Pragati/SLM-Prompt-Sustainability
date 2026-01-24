import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):

    def test_get_median_even_length(self):
        self.assertEqual(get_median([1, 2, 3, 4], [5, 6, 7, 8], 4), (2.5, 5.5))
        self.assertEqual(get_median([1, 2, 3, 4], [5, 6, 7, 8], 3), (2.0, 5.0))
        self.assertEqual(get_median([1, 2, 3, 4], [5, 6, 7, 8], 2), (2.0, 5.0))
        self.assertEqual(get_median([1, 2, 3, 4], [5, 6, 7, 8], 1), (2.0, 5.0))

    def test_get_median_odd_length(self):
        self.assertEqual(get_median([1, 2, 3, 4], [5, 6, 7], 4), (2.5, 5.5))
        self.assertEqual(get_median([1, 2, 3, 4], [5, 6, 7], 3), (2.0, 5.0))
        self.assertEqual(get_median([1, 2, 3, 4], [5, 6, 7], 2), (2.0, 5.0))
        self.assertEqual(get_median([1, 2, 3, 4], [5, 6, 7], 1), (2.0, 5.0))

    def test_get_median_empty_arrays(self):
        self.assertEqual(get_median([], [], 0), (None, None))
        self.assertEqual(get_median([], [1], 1), (None, 1))
        self.assertEqual(get_median([1], [], 1), (1, None))

    def test_get_median_single_array(self):
        self.assertEqual(get_median([1], [], 1), (1, None))
        self.assertEqual(get_median([], [1], 1), (None, 1))
        self.assertEqual(get_median([1, 2], [], 1), (1, None))
        self.assertEqual(get_median([], [1, 2], 1), (None, 1))
        self.assertEqual(get_median([1, 2], [3], 1), (1.5, 3))
        self.assertEqual(get_median([3], [1, 2], 1), (1.5, 3))
