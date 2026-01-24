import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_max_sum(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)
        self.assertEqual(max_sum([-1, -2, -3, -4, -5], 5), -1)
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6], 6), 9)
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7], 7), 9)
        self.assertEqual(max_sum([-1, -2, -3, -4, -5, -6, -7], 7), -1)
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8], 8), 9)
        self.assertEqual(max_sum([-1, -2, -3, -4, -5, -6, -7, -8], 8), -1)
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)
        self.assertEqual(max_sum([-1, -2, -3, -4, -5, -6, -7, -8, -9], 9), -1)
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 9)
        self.assertEqual(max_sum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 10), -1)
