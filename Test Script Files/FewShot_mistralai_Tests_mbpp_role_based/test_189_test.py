import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(first_Missing_Positive([3, 5, 6, 1, 2], 5), 4)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4], 4), 1)
        self.assertEqual(first_Missing_Positive([-1, 0, 3, 5, 6], 5), 1)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5], 5), 6)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6], 6), 7)

    def test_empty_list(self):
        self.assertEqual(first_Missing_Positive([], 0), 1)

    def test_single_zero(self):
        self.assertEqual(first_Missing_Positive([0], 1), 1)

    def test_all_zero(self):
        self.assertEqual(first_Missing_Positive([0, 0, 0], 3), 1)

    def test_all_negative(self):
        self.assertEqual(first_Missing_Positive([-1, -2, -3], 3), 1)

    def test_all_large_numbers(self):
        self.assertEqual(first_Missing_Positive([1000000, 1000001, 1000002], 3), 1)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            first_Missing_Positive([1, 2, 3], -1)
