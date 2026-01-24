import unittest
from mbpp_850_code import is_triangleexists

class TestTriangleExistence(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(is_triangleexists(60, 60, 60))

    def test_invalid_triangle(self):
        self.assertFalse(is_triangleexists(100, 70, 10))

    def test_zero_sides(self):
        self.assertFalse(is_triangleexists(0, 0, 0))

    def test_sum_not_180(self):
        self.assertFalse(is_triangleexists(50, 50, 80))

    def test_negative_sides(self):
        self.assertFalse(is_triangleexists(-10, 20, 30))
