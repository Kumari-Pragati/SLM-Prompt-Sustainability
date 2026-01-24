import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_isosceles(3, 3, 2))

    def test_edge_case_with_zero(self):
        self.assertFalse(check_isosceles(0, 0, 2))

    def test_edge_case_with_negative_numbers(self):
        self.assertFalse(check_isosceles(-1, -1, -2))

    def test_edge_case_with_equal_numbers(self):
        self.assertTrue(check_isosceles(1, 1, 1))

    def test_edge_case_with_zero_and_negative(self):
        self.assertFalse(check_isosceles(0, -1, -2))

    def test_error_case_with_non_numeric_input(self):
        with self.assertRaises(TypeError):
            check_isosceles("a", 2, 3)
