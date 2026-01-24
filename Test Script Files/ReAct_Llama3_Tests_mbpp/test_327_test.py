import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_isosceles_true(self):
        self.assertTrue(check_isosceles(3, 3, 4))

    def test_isosceles_false(self):
        self.assertFalse(check_isosceles(1, 2, 3))

    def test_isosceles_equal_sides(self):
        self.assertTrue(check_isosceles(4, 4, 4))

    def test_isosceles_one_equal_side(self):
        self.assertTrue(check_isosceles(3, 3, 5))

    def test_isosceles_no_equal_sides(self):
        self.assertFalse(check_isosceles(1, 2, 3))

    def test_isosceles_negative_sides(self):
        self.assertFalse(check_isosceles(-1, -2, -3))

    def test_isosceles_zero_sides(self):
        self.assertFalse(check_isosceles(0, 0, 0))
