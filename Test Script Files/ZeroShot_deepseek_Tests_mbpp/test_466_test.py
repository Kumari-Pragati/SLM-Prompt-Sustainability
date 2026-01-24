import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):

    def test_find_peak(self):
        self.assertEqual(find_peak([1, 3, 20, 4, 1, 0], 6), 2)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(find_peak([6, 5, 4, 3, 2, 1], 6), 0)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 8)
        self.assertEqual(find_peak([10, 8, 6, 4, 2, 1, 0], 7), 0)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 9)
        self.assertEqual(find_peak([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10), 0)
        self.assertEqual(find_peak([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10), 0)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 10)
        self.assertEqual(find_peak([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 11), 0)
