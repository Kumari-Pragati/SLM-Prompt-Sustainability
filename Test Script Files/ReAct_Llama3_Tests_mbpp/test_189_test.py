import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(first_Missing_Positive([], 10), 1)

    def test_single_element_array(self):
        self.assertEqual(first_Missing_Positive([1], 10), 2)

    def test_array_with_missing_positive(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5], 5), 6)

    def test_array_with_duplicates(self):
        self.assertEqual(first_Missing_Positive([1, 2, 2, 3, 4, 5], 5), 6)

    def test_array_with_out_of_range(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 7], 5), 6)

    def test_array_with_out_of_range_and_duplicates(self):
        self.assertEqual(first_Missing_Positive([1, 2, 2, 3, 4, 5, 7], 5), 6)

    def test_array_with_out_of_range_and_duplicates_and_missing_positive(self):
        self.assertEqual(first_Missing_Positive([1, 2, 2, 3, 4, 5, 7, 8], 5), 9)
