import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):

    def test_typical_valid(self):
        self.assertTrue(validity_triangle(60, 60, 60))

    def test_typical_invalid(self):
        self.assertFalse(validity_triangle(100, 100, 100))

    def test_edge_case_valid(self):
        self.assertTrue(validity_triangle(90, 60, 30))

    def test_edge_case_invalid(self):
        self.assertFalse(validity_triangle(100, 100, 100))

    def test_edge_case_equal(self):
        self.assertTrue(validity_triangle(90, 90, 0))

    def test_edge_case_zero(self):
        with self.assertRaises(TypeError):
            validity_triangle(0, 0, 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            validity_triangle(-1, -1, -1)
