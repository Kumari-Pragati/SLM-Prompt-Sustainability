import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_non_equilateral_triangle(self):
        self.assertFalse(check_equilateral(3, 4, 5))

    def test_invalid_input_less_than_zero(self):
        self.assertRaises(ValueError, check_equilateral, -1, 2, 3)

    def test_invalid_input_more_than_zero(self):
        self.assertRaises(ValueError, check_equilateral, 10, 2, 3)

    def test_invalid_input_different_types(self):
        self.assertRaises(TypeError, check_equilateral, 3, 'a', 4)
