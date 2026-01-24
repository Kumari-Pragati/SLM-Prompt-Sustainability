import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):
    def test_simple_positive(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5], 5), 6)

    def test_simple_negative(self):
        self.assertEqual(first_Missing_Positive([-1, -2, -3, -4, -5], 5), 1)

    def test_empty_array(self):
        self.assertEqual(first_Missing_Positive([], 5), 1)

    def test_single_element_array(self):
        self.assertEqual(first_Missing_Positive([1], 1), 2)

    def test_all_positive(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5], 5), 6)

    def test_all_negative(self):
        self.assertEqual(first_Missing_Positive([-1, -2, -3, -4, -5], 5), 1)

    def test_max_value(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5], 5), 6)

    def test_max_value_negative(self):
        self.assertEqual(first_Missing_Positive([-1, -2, -3, -4, -5], 5), 1)

    def test_max_value_zero(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 0], 5), 6)

    def test_max_value_zero_negative(self):
        self.assertEqual(first_Missing_Positive([-1, -2, -3, -4, 0], 5), 1)
