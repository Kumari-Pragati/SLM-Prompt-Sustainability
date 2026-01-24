import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_isosceles(3, 3, 2))

    def test_edge_case(self):
        self.assertTrue(check_isosceles(0, 0, 0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_isosceles("3", 3, 2)

    def test_negative_numbers(self):
        self.assertTrue(check_isosceles(-3, -3, 2))

    def test_equal_sides(self):
        self.assertTrue(check_isosceles(5, 5, 5))

    def test_not_isosceles(self):
        self.assertFalse(check_isosceles(3, 4, 5))
