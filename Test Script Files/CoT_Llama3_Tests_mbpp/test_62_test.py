import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):
    def test_smallest_num(self):
        self.assertEqual(smallest_num([1, 2, 3, 4, 5]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(smallest_num([5, 3, 2, 1]), 1)
        self.assertEqual(smallest_num([-5, -3, -2, -1]), -5)
        self.assertEqual(smallest_num([1, 1, 1, 1, 1]), 1)
        self.assertEqual(smallest_num([-1, -1, -1, -1, -1]), -1)
        self.assertEqual(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -10)
        self.assertEqual(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]), -15)
        self.assertEqual(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]), -16)
        self.assertEqual(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17]), -17)
        self.assertEqual(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18]), -18)
        self.assertEqual(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19]), -19)
        self.assertEqual(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]), -20)
        self.assertEqual(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,