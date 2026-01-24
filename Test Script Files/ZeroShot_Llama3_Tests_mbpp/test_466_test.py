import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):

    def test_find_peak(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(find_peak([5, 4, 3, 2, 1], 5), 0)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7], 7), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8], 8), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 21), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 22), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,