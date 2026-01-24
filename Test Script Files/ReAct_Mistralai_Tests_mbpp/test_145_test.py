import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_Abs_Diff([]), 0)

    def test_single_element(self):
        for num in range(10):
            self.assertEqual(max_Abs_Diff([num], 1), 0)

    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(max_Abs_Diff(arr, len(arr)), 4)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(max_Abs_Diff(arr, len(arr)), 4)

    def test_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        self.assertEqual(max_Abs_Diff(arr, len(arr)), 5)

    def test_zero_in_list(self):
        arr = [0, 1, 2, 3, 4]
        self.assertEqual(max_Abs_Diff(arr, len(arr)), 4)

    def test_negative_n(self):
        self.assertRaises(IndexError, lambda: max_Abs_Diff([1, 2, 3], -1))

    def test_empty_n(self):
        self.assertRaises(ValueError, lambda: max_Abs_Diff([1, 2, 3], 0))

    def test_non_iterable_input(self):
        self.assertRaises(TypeError, lambda: max_Abs_Diff(123, 456))
