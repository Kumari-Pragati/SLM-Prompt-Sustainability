import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertTrue(validity_triangle(60, 60, 60))

    def test_invalid_triangle(self):
        self.assertFalse(validity_triangle(100, 100, 100))

    def test_edge_case(self):
        self.assertTrue(validity_triangle(90, 60, 30))

    def test_edge_case2(self):
        self.assertTrue(validity_triangle(30, 60, 90))

    def test_edge_case3(self):
        self.assertTrue(validity_triangle(90, 30, 60))

    def test_invalid_triangle2(self):
        self.assertFalse(validity_triangle(100, 100, 1000))

    def test_invalid_triangle3(self):
        self.assertFalse(validity_triangle(100, 1000, 100))

    def test_invalid_triangle4(self):
        self.assertFalse(validity_triangle(1000, 100, 100))
