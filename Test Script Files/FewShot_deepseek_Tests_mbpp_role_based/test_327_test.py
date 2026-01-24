import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_isosceles(3, 3, 2))

    def test_all_sides_equal(self):
        self.assertTrue(check_isosceles(1, 1, 1))

    def test_two_sides_equal(self):
        self.assertTrue(check_isosceles(2, 2, 3))

    def test_no_sides_equal(self):
        self.assertFalse(check_isosceles(1, 2, 3))

    def test_zero_length_sides(self):
        self.assertFalse(check_isosceles(0, 0, 0))

    def test_negative_length_sides(self):
        self.assertFalse(check_isosceles(-1, -2, -3))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_isosceles("a", 2, 3)
