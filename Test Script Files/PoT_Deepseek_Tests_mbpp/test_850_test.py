import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_triangleexists(60, 60, 60))
        self.assertTrue(is_triangleexists(1, 1, 178))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(is_triangleexists(0, 0, 0))
        self.assertFalse(is_triangleexists(1, 1, 181))
        self.assertFalse(is_triangleexists(1, 181, 1))
        self.assertFalse(is_triangleexists(181, 1, 1))

    def test_invalid_or_exceptional_inputs(self):
        self.assertFalse(is_triangleexists(-1, 1, 1))
        self.assertFalse(is_triangleexists(1, -1, 1))
        self.assertFalse(is_triangleexists(1, 1, -1))
