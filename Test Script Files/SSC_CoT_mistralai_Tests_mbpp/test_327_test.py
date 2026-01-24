import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_isosceles_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_equilateral_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 4))
        self.assertTrue(check_isosceles(4, 3, 3))
        self.assertTrue(check_isosceles(3, 4, 3))

    def test_isosceles_with_equal_sides(self):
        self.assertTrue(check_isosceles(3, 3, 4))
        self.assertTrue(check_isosceles(3, 4, 3))
        self.assertTrue(check_isosceles(4, 3, 3))

    def test_isosceles_with_almost_equal_sides(self):
        self.assertTrue(check_isosceles(3.001, 3, 3))
        self.assertTrue(check_isosceles(3, 3.001, 3))
        self.assertTrue(check_isosceles(3, 3, 3.001))

    def test_not_isosceles(self):
        self.assertFalse(check_isosceles(3, 4, 5))
        self.assertFalse(check_isosceles(4, 5, 3))
        self.assertFalse(check_isosceles(5, 3, 4))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_isosceles, 'a', 3, 4)
        self.assertRaises(TypeError, check_isosceles, 3, 'b', 4)
        self.assertRaises(TypeError, check_isosceles, 3, 4, 'c')
