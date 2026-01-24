import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(validity_triangle(60, 60, 60))

    def test_invalid_triangle(self):
        self.assertFalse(validity_triangle(90, 90, 90))

    def test_edge_case_triangle(self):
        self.assertTrue(validity_triangle(90, 30, 60))

    def test_edge_case_triangle2(self):
        self.assertTrue(validity_triangle(30, 90, 60))

    def test_edge_case_triangle3(self):
        self.assertTrue(validity_triangle(60, 90, 30))

    def test_edge_case_triangle4(self):
        self.assertTrue(validity_triangle(30, 30, 120))

    def test_edge_case_triangle5(self):
        self.assertFalse(validity_triangle(120, 30, 30))

    def test_edge_case_triangle6(self):
        self.assertFalse(validity_triangle(30, 120, 30))

    def test_edge_case_triangle7(self):
        self.assertFalse(validity_triangle(30, 30, 150))

    def test_edge_case_triangle8(self):
        self.assertFalse(validity_triangle(150, 30, 30))

    def test_edge_case_triangle9(self):
        self.assertFalse(validity_triangle(30, 30, 180))

    def test_edge_case_triangle10(self):
        self.assertTrue(validity_triangle(180, 0, 0))

    def test_edge_case_triangle11(self):
        self.assertTrue(validity_triangle(0, 180, 0))

    def test_edge_case_triangle12(self):
        self.assertTrue(validity_triangle(0, 0, 180))
