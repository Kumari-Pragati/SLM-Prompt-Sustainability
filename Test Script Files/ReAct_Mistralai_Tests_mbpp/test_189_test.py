import unittest
from189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(first_Missing_Positive([], 0), 1)

    def test_all_negative_numbers(self):
        self.assertEqual(first_Missing_Positive([-1, -2, -3], 3), 1)

    def test_all_positive_numbers_less_than_n(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3], 4), 4)

    def test_all_positive_numbers_equal_to_n(self):
        self.assertEqual(first_Missing_Positive([4, 4, 4, 4], 4), 1)

    def test_all_positive_numbers_greater_than_n(self):
        self.assertEqual(first_Missing_Positive([5, 6, 7], 3), 1)

    def test_single_zero(self):
        self.assertEqual(first_Missing_Positive([0], 1), 1)

    def test_single_one(self):
        self.assertEqual(first_Missing_Positive([1], 1), 2)

    def test_single_number_greater_than_n(self):
        self.assertEqual(first_Missing_Positive([10], 9), 1)

    def test_multiple_numbers_less_than_one(self):
        self.assertEqual(first_Missing_Positive([-1, -2], 2), 1)

    def test_multiple_numbers_greater_than_n(self):
        self.assertEqual(first_Missing_Positive([11, 12, 13], 10), 1)

    def test_duplicate_numbers(self):
        self.assertEqual(first_Missing_Positive([2, 2, 3], 3), 1)
