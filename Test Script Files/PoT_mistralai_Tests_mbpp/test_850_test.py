import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleexists(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_triangleexists(3, 4, 5))
        self.assertTrue(is_triangleexists(6, 8, 10))
        self.assertTrue(is_triangleexists(7, 24, 25))

    def test_edge_cases(self):
        self.assertFalse(is_triangleexists(0, 0, 0))
        self.assertFalse(is_triangleexists(0, 3, 4))
        self.assertFalse(is_triangleexists(3, 0, 4))
        self.assertFalse(is_triangleexists(3, 4, 0))
        self.assertFalse(is_triangleexists(179, 1, 2))
        self.assertFalse(is_triangleexists(3, 4, 179))
        self.assertFalse(is_triangleexists(1, 2, 178))

    def test_boundary_cases(self):
        self.assertTrue(is_triangleexists(17, 18, 17))
        self.assertTrue(is_triangleexists(17, 18, 16))
        self.assertFalse(is_triangleexists(17, 18, 19))
