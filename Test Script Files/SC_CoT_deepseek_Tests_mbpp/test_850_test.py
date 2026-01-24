import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertTrue(is_triangleexists(60, 60, 60))

    def test_boundary_conditions(self):
        self.assertFalse(is_triangleexists(0, 0, 0))
        self.assertFalse(is_triangleexists(180, 0, 0))
        self.assertFalse(is_triangleexists(0, 180, 0))
        self.assertFalse(is_triangleexists(0, 0, 180))
        self.assertFalse(is_triangleexists(180, 180, 180))

    def test_edge_cases(self):
        self.assertFalse(is_triangleexists(1, 1, 1))
        self.assertFalse(is_triangleexists(1, 1, 179))
        self.assertFalse(is_triangleexists(179, 1, 1))
        self.assertFalse(is_triangleexists(1, 179, 1))
        self.assertFalse(is_triangleexists(179, 179, 1))
        self.assertFalse(is_triangleexists(179, 1, 179))
        self.assertFalse(is_triangleexists(1, 179, 179))
        self.assertFalse(is_triangleexists(179, 179, 179))

    def test_invalid_inputs(self):
        self.assertFalse(is_triangleexists(-1, 1, 1))
        self.assertFalse(is_triangleexists(1, -1, 1))
        self.assertFalse(is_triangleexists(1, 1, -1))
        self.assertFalse(is_triangleexists(181, 1, 1))
        self.assertFalse(is_triangleexists(1, 181, 1))
        self.assertFalse(is_triangleexists(1, 1, 181))
