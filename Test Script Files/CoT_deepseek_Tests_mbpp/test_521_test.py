import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_isosceles(3, 3, 2))

    def test_edge_case(self):
        self.assertFalse(check_isosceles(1, 2, 3))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_isosceles("a", 2, 3)

    def test_negative_numbers(self):
        self.assertTrue(check_isosceles(-1, -1, 2))

    def test_zero(self):
        self.assertFalse(check_isosceles(0, 2, 2))
