import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(check_Validity(3, 4, 5))

    def test_invalid_triangle(self):
        self.assertFalse(check_Validity(1, 2, 5))

    def test_zero_length_sides(self):
        self.assertFalse(check_Validity(0, 0, 0))

    def test_negative_length_sides(self):
        self.assertFalse(check_Validity(-1, -2, -3))

    def test_large_numbers(self):
        self.assertTrue(check_Validity(1000000, 2000000, 3000000))

    def test_equal_sides(self):
        self.assertFalse(check_Validity(5, 5, 5))
