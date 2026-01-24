import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_isosceles_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 4))
        self.assertTrue(check_isosceles(4, 4, 5))
        self.assertTrue(check_isosceles(5, 5, 6))

    def test_equilateral_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_isosceles_with_equal_and_different(self):
        self.assertTrue(check_isosceles(3, 3, 4))
        self.assertTrue(check_isosceles(3, 4, 3))
        self.assertTrue(check_isosceles(4, 3, 3))

    def test_non_isosceles_triangle(self):
        self.assertFalse(check_isosceles(3, 4, 5))
        self.assertFalse(check_isosceles(4, 5, 3))
        self.assertFalse(check_isosceles(5, 3, 4))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_isosceles, 'a', 'b', 'c')
        self.assertRaises(TypeError, check_isosceles, 3, 'b', 'c')
        self.assertRaises(TypeError, check_isosceles, 3, 4, 'c')
