import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 4), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 5), 3.5)

    def test_edge_cases(self):
        self.assertEqual(get_median([], [], 0), -1)
        self.assertEqual(get_median([1], [], 1), 1)
        self.assertEqual(get_median([1], [2], 1), 1.5)
        self.assertEqual(get_median([1], [2], 2), 1.5)
        self.assertEqual(get_median([1], [2], 3), 1.5)
        self.assertEqual(get_median([1, 2], [], 2), 1.5)
        self.assertEqual(get_median([1, 2], [3], 2), 2.0)
        self.assertEqual(get_median([1, 2], [3], 3), 2.0)

    def test_corner_cases(self):
        self.assertEqual(get_median([1, 2, 3], [4, 5, 6], 3), 3.0)
        self.assertEqual(get_median([1, 2, 3], [4, 5, 6], 4), 3.0)
        self.assertEqual(get_median([1, 2, 3], [4, 5, 6], 5), 3.0)
        self.assertEqual(get_median([1, 2, 3], [4, 5, 6], 6), 3.0)
        self.assertEqual(get_median([1, 2, 3], [4, 5, 6], 7), 3.0)
