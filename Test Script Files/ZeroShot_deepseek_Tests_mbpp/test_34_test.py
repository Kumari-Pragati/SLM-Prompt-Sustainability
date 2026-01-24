import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_find_missing_1(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 6], 6), 5)

    def test_find_missing_2(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35], 35), 34)

    def test_find_missing_3(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36], 36), -1)

    def test_find_missing_4(self):
        self.assertEqual(find_missing([1], 1), -1)

    def test_find_missing_5(self):
        self.assertEqual(find_missing([], 0), -1)
