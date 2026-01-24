import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_Abs_Diff([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_Abs_Diff([1], 1), 0)

    def test_positive_numbers(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5], 5), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5], 5), 6)

    def test_mixed_numbers(self):
        self.assertEqual(max_Abs_Diff([1, -2, 3, -4, 5], 5), 7)

    def test_duplicate_elements(self):
        self.assertEqual(max_Abs_Diff([1, 1, 2, 2, 3], 5), 2)

    def test_large_numbers(self):
        self.assertEqual(max_Abs_Diff([1000000001, -1000000001, 0, 1000000002], 4), 2000000003)

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            max_Abs_Diff([1, 2, 3], 4)

    def test_invalid_input_negative_length(self):
        with self.assertRaises(ValueError):
            max_Abs_Diff([1, 2, 3], -1)
