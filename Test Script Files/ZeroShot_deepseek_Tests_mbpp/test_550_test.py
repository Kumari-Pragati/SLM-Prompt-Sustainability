import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):

    def test_find_Max(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 0, 4), 5)
        self.assertEqual(find_Max([1, 2, 5, 4, 3], 0, 4), 5)
        self.assertEqual(find_Max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9), 10)
        self.assertEqual(find_Max([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 9), 10)
        self.assertEqual(find_Max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 0, 10), 11)
        self.assertEqual(find_Max([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 10), 11)
        self.assertEqual(find_Max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 0, 11), 12)
        self.assertEqual(find_Max([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 11), 12)
