import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_max_sum(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(max_sum([5, 4, 3, 2, 1], 5), 15)
        self.assertEqual(max_sum([1, 3, 5, 7, 9], 5), 24)
        self.assertEqual(max_sum([9, 7, 5, 3, 1], 5), 24)
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 55)
        self.assertEqual(max_sum([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10), 55)
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 4, 3, 2, 1], 9), 18)
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 55)
        self.assertEqual(max_sum([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10), 55)
