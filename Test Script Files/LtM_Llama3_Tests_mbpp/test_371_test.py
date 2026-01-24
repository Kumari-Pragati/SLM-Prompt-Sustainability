import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):
    def test_smallest_missing(self):
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5], 1, 5), 6)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6], 1, 6), 7)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7], 1, 7), 8)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8], 1, 8), 9)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 9), 10)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 10), 11)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 1, 11), 12)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 1, 12), 13)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 1, 13), 14)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 1, 14), 15)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 1, 15), 16)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 1, 16), 17)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 1, 17), 18)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 1, 18), 19)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 1, 19), 20)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 1, 20), 21)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 1, 21), 22)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 1, 22),