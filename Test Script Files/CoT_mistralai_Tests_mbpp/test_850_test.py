import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleexists(unittest.TestCase):

    def test_positive(self):
        self.assertTrue(is_triangleexists(3, 4, 5))
        self.assertTrue(is_triangleexists(6, 8, 10))
        self.assertTrue(is_triangleexists(7, 24, 25))

    def test_edge_cases(self):
        self.assertTrue(is_triangleexists(17, 17, 180 - 17))
        self.assertTrue(is_triangleexists(17, 17, 180 - 18))
        self.assertTrue(is_triangleexists(17, 17, 180 - 17 + 1e-6))

    def test_invalid_inputs(self):
        self.assertFalse(is_triangleexists(0, 0, 0))
        self.assertFalse(is_triangleexists(0, 0, 180))
        self.assertFalse(is_triangleexists(180, 0, 0))
        self.assertFalse(is_triangleexists(180, 180, 0))
        self.assertFalse(is_triangleexists(-1, 1, 1))
        self.assertFalse(is_triangleexists(1, -1, 1))
        self.assertFalse(is_triangleexists(1, 1, -1))
        self.assertFalse(is_triangleexists(181, 17, 16))
        self.assertFalse(is_triangleexists(17, 181, 16))
        self.assertFalse(is_triangleexists(17, 17, 181))
