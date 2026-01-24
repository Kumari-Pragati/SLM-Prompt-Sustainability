import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleexists(unittest.TestCase):

    def test_simple_triangle(self):
        self.assertTrue(is_triangleexists(3, 4, 5))
        self.assertTrue(is_triangleexists(6, 8, 10))
        self.assertTrue(is_triangleexists(7, 24, 25))

    def test_degenerate_triangle(self):
        self.assertTrue(is_triangleexists(3, 3, 3))
        self.assertTrue(is_triangleexists(0, 0, 0))
        self.assertTrue(is_triangleexists(179, 1, 180))

    def test_invalid_inputs(self):
        self.assertFalse(is_triangleexists(0, 0, 181))
        self.assertFalse(is_triangleexists(-1, 2, 3))
        self.assertFalse(is_triangleexists(1, 0, 0))
        self.assertFalse(is_triangleexists(1, 1, 0))
        self.assertFalse(is_triangleexists(1, 1, 181))
