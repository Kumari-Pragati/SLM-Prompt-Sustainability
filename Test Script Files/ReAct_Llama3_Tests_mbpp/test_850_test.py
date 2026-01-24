import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(is_triangleexists(60, 60, 60))

    def test_invalid_triangle(self):
        self.assertFalse(is_triangleexists(0, 0, 0))

    def test_zero_angle(self):
        self.assertFalse(is_triangleexists(90, 0, 0))

    def test_nonzero_angles(self):
        self.assertFalse(is_triangleexists(90, 90, 0))

    def test_valid_triangle_with_zero_angle(self):
        self.assertTrue(is_triangleexists(60, 60, 0))

    def test_invalid_triangle_with_zero_angle(self):
        self.assertFalse(is_triangleexists(0, 0, 0))

    def test_edge_case(self):
        self.assertTrue(is_triangleexists(90, 90, 90))

    def test_edge_case_with_zero_angle(self):
        self.assertFalse(is_triangleexists(90, 0, 0))
