import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(is_triangleexists(3, 4, 5))
        self.assertTrue(is_triangleexists(6, 8, 10))
        self.assertTrue(is_triangleexists(12, 16, 20))

    def test_degenerate_triangle(self):
        self.assertTrue(is_triangleexists(0, 0, 0))
        self.assertTrue(is_triangleexists(0, 0, 180))
        self.assertTrue(is_triangleexists(180, 0, 0))

    def test_non_triangle(self):
        self.assertFalse(is_triangleexists(3, 4, 6))
        self.assertFalse(is_triangleexists(4, 5, 6))
        self.assertFalse(is_triangleexists(6, 5, 4))

    def test_invalid_input(self):
        self.assertFalse(is_triangleexists(-1, 2, 3))
        self.assertFalse(is_triangleexists(1, -2, 3))
        self.assertFalse(is_triangleexists(1, 2, -3))
        self.assertFalse(is_triangleexists(0, 0, 181))
