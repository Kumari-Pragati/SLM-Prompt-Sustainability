import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5], 5), 6)
        self.assertEqual(max_Abs_Diff([0, 0, 0, 0, 0], 5), 0)

    def test_single_element(self):
        self.assertEqual(max_Abs_Diff([1], 1), 0)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            max_Abs_Diff([], 0)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            max_Abs_Diff([1, 2, 3], -1)

    def test_negative_numbers(self):
        self.assertEqual(max_Abs_Diff([-1, -2, -3], 3), 3)
