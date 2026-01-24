import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_isosceles_true(self):
        self.assertTrue(check_isosceles(3, 3, 4))

    def test_isosceles_false(self):
        self.assertFalse(check_isosceles(1, 2, 3))

    def test_isosceles_equal_sides(self):
        self.assertTrue(check_isosceles(2, 2, 2))

    def test_isosceles_reverse_order(self):
        self.assertTrue(check_isosceles(4, 3, 3))

    def test_isosceles_invalid_input(self):
        with self.assertRaises(TypeError):
            check_isosceles('a', 2, 3)

    def test_isosceles_negative_numbers(self):
        self.assertTrue(check_isosceles(-2, -2, 3))
