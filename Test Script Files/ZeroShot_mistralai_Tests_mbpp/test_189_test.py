import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(first_Missing_Positive([], 0), 1)

    def test_all_positive(self):
        self.assertEqual(first_Missing_Positive([2, 3, 4, 6, 7, 8, 10], 7), 9)

    def test_all_negative(self):
        self.assertEqual(first_Missing_Positive([-1, -2, -3], 3), 1)

    def test_all_zero(self):
        self.assertEqual(first_Missing_Positive([0, 0, 0], 3), 1)

    def test_single_negative(self):
        self.assertEqual(first_Missing_Positive([-1, 1, 2], 3), 3)

    def test_single_zero(self):
        self.assertEqual(first_Missing_Positive([0, 1, 2], 3), 4)

    def test_single_positive(self):
        self.assertEqual(first_Missing_Positive([1], 1), 2)

    def test_multiple_missing(self):
        self.assertEqual(first_Missing_Positive([3, 5, 6], 3), 1)

    def test_large_input(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 5, 6, 8, 9], 7), 4)
