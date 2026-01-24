import unittest
from850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):

    def test_zero_arguments(self):
        self.assertFalse(is_triangleexists(0, 0, 0))

    def test_negative_arguments(self):
        self.assertFalse(is_triangleexists(-1, -2, -3))

    def test_non_sum_of_180_degrees(self):
        self.assertFalse(is_triangleexists(3, 4, 10))

    def test_invalid_triangle(self):
        self.assertFalse(is_triangleexists(3, 4, 5))

    def test_valid_triangle_1(self):
        self.assertTrue(is_triangleexists(3, 4, 5))

    def test_valid_triangle_2(self):
        self.assertTrue(is_triangleexists(6, 8, 10))

    def test_valid_triangle_3(self):
        self.assertTrue(is_triangleexists(12, 16, 20))
