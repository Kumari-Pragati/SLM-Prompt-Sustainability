import unittest
from mbpp_850_code import MagicMock

from850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(is_triangleexists(3, 4, 5))
        self.assertTrue(is_triangleexists(6, 8, 10))
        self.assertTrue(is_triangleexists(12, 16, 20))

    def test_edge_cases(self):
        self.assertFalse(is_triangleexists(0, 0, 0))
        self.assertFalse(is_triangleexists(0, 3, 3))
        self.assertFalse(is_triangleexists(3, 0, 0))
        self.assertFalse(is_triangleexists(3.14, 4, 5))
        self.assertFalse(is_triangleexists(-3, 4, 5))
        self.assertFalse(is_triangleexists(3, -4, 5))
        self.assertFalse(is_triangleexists(3, 4, -5))

    def test_boundary_conditions(self):
        self.assertFalse(is_triangleexists(179, 1, 179))
        self.assertFalse(is_triangleexists(1, 179, 179))
        self.assertFalse(is_triangleexists(179, 179, 1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_triangleexists('a', 'b', 'c')
        with self.assertRaises(TypeError):
            is_triangleexists([1, 2, 3])
        with self.assertRaises(TypeError):
            is_triangleexists(1, MagicMock(), 3)
