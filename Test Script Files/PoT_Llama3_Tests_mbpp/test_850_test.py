import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_triangleexists(60, 60, 60))

    def test_edge_case_a_zero(self):
        self.assertFalse(is_triangleexists(0, 60, 60))

    def test_edge_case_b_zero(self):
        self.assertFalse(is_triangleexists(60, 0, 60))

    def test_edge_case_c_zero(self):
        self.assertFalse(is_triangleexists(60, 60, 0))

    def test_edge_case_a_b_c_zero(self):
        self.assertFalse(is_triangleexists(0, 0, 0))

    def test_edge_case_a_b_c_not_180(self):
        self.assertFalse(is_triangleexists(30, 30, 120))

    def test_edge_case_a_b_c_180(self):
        self.assertTrue(is_triangleexists(30, 30, 120))

    def test_edge_case_a_b_c_180_not_valid(self):
        self.assertFalse(is_triangleexists(30, 30, 30))

    def test_edge_case_a_b_c_180_valid(self):
        self.assertTrue(is_triangleexists(30, 30, 120))

    def test_edge_case_a_b_c_180_valid2(self):
        self.assertTrue(is_triangleexists(30, 120, 30))

    def test_edge_case_a_b_c_180_valid3(self):
        self.assertTrue(is_triangleexists(120, 30, 30))

    def test_edge_case_a_b_c_180_valid4(self):
        self.assertTrue(is_triangleexists(30, 30, 120))
