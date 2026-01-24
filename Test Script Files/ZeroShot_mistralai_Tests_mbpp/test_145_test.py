import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_Abs_Diff([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_Abs_Diff([1], 1), 0)

    def test_positive_numbers(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4], 4), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4], 4), 7)

    def test_mixed_numbers(self):
        self.assertEqual(max_Abs_Diff([1, -2, 3, -4], 4), 5)

    def test_large_numbers(self):
        self.assertEqual(max_Abs_Diff([1000000001, -1000000001], 2), 2000000002)
