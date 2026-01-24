import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_triangleexists(60, 60, 60))

    def test_edge_case(self):
        self.assertFalse(is_triangleexists(0, 0, 0))
        self.assertFalse(is_triangleexists(180, 0, 0))
        self.assertFalse(is_triangleexists(0, 180, 0))
        self.assertFalse(is_triangleexists(0, 0, 180))
        self.assertFalse(is_triangleexists(90, 90, 91))

    def test_invalid_input(self):
        self.assertFalse(is_triangleexists('a', 60, 60))
        self.assertFalse(is_triangleexists(60, 'b', 60))
        self.assertFalse(is_triangleexists(60, 60, 'c'))
        self.assertFalse(is_triangleexists(60, 'b', 'c'))
        self.assertFalse(is_triangleexists('a', 60, 'c'))
        self.assertFalse(is_triangleexists('a', 'b', 60))
        self.assertFalse(is_triangleexists('a', 'b', 'c'))
