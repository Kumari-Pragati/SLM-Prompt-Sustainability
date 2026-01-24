import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sum([[1]], 1), 1)

    def test_small_list(self):
        self.assertEqual(max_sum([[1, 2], [3, 4]], 2), 7)

    def test_large_list(self):
        self.assertEqual(max_sum([[1, 2, 3, 4, 5], [8, 9, 4, 7, 5], [7, 2, 6, 3, 9], [4, 5, 1, 8, 5], [5, 6, 2, 1, 9]], 5), 28)
