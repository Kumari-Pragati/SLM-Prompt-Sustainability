import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_isosceles_triangle(self):
        self.assertTrue(check_isosceles(5, 5, 7))

    def test_equilateral_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_scalene_triangle(self):
        self.assertFalse(check_isosceles(4, 5, 6))

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            check_isosceles('a', 'b', 'c')

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            check_isosceles(0, 0, 0)
