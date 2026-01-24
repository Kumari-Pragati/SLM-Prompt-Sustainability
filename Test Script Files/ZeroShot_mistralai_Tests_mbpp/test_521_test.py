import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_isosceles_triangle(self):
        self.assertTrue(check_isosceles(5, 5, 7))
        self.assertTrue(check_isosceles(3, 3, 4))
        self.assertTrue(check_isosceles(6, 6, 5))

    def test_not_isosceles_triangle(self):
        self.assertFalse(check_isosceles(5, 6, 7))
        self.assertFalse(check_isosceles(3, 4, 5))
        self.assertFalse(check_isosceles(6, 7, 5))
        self.assertFalse(check_isosceles(2, 2, 3))
        self.assertFalse(check_isosceles(4, 4, 5))
        self.assertFalse(check_isosceles(7, 7, 6))
