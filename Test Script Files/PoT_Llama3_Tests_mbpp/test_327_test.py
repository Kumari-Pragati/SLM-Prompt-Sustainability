import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_typical_isosceles(self):
        self.assertTrue(check_isosceles(3, 3, 5))

    def test_typical_non_isosceles(self):
        self.assertFalse(check_isosceles(3, 4, 5))

    def test_edge_isosceles(self):
        self.assertTrue(check_isosceles(2, 2, 2))

    def test_edge_non_isosceles(self):
        self.assertFalse(check_isosceles(1, 2, 3))

    def test_corner_equal_sides(self):
        self.assertTrue(check_isosceles(4, 4, 4))

    def test_corner_non_equal_sides(self):
        self.assertFalse(check_isosceles(3, 4, 5))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_isosceles('a', 'b', 'c')
