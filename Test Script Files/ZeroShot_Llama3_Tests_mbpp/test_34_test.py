import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_find_missing(self):
        self.assertEqual(find_missing([1, 2, 3, 5, 6], 6), 4)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 7, 8], 8), 6)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 8, 9], 9), 7)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 0)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12, 11), 13)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15, 14), 16)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20, 19), 21)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 25, 24), 26)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 30, 29), 31)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], 35, 34), 36)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 50, 49), 51)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], 60, 59), 61)
        self.assertEqual(find_missing([1, 2