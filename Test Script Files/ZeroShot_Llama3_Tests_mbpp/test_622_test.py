import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):

    def test_get_median(self):
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7], 4), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8], 5), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9], 6), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10], 7), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11], 8), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12], 9), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13], 10), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14], 11), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 12), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 13), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 14), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 15), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 16), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 17), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 18), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 19), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,