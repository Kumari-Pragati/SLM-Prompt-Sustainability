import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(first_Missing_Positive([], 0), 1)

    def test_all_negative(self):
        self.assertEqual(first_Missing_Positive([-1, -2, -3], 3), 1)

    def test_all_positive_less_than_n(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3], 4), 4)

    def test_all_positive_greater_than_n(self):
        self.assertEqual(first_Missing_Positive([5, 6, 7], 3), 1)

    def test_single_zero(self):
        self.assertEqual(first_Missing_Positive([0], 1), 1)

    def test_single_one(self):
        self.assertEqual(first_Missing_Positive([1], 1), 2)

    def test_single_greater_than_n(self):
        self.assertEqual(first_Missing_Positive([4], 3), 1)

    def test_multiple_missing(self):
        self.assertEqual(first_Missing_Positive([3, 5, 6], 6), 1)

    def test_invalid_input_negative_list_length(self):
        with self.assertRaises(ValueError):
            first_Missing_Positive([-1, -2], -1)

    def test_invalid_input_non_integer_list(self):
        with self.assertRaises(TypeError):
            first_Missing_Positive([1.5, 2.5, 3.5], 3)
