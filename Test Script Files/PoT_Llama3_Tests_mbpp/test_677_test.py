import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):
    def test_typical_valid(self):
        self.assertTrue(validity_triangle(60, 60, 60))

    def test_typical_invalid(self):
        self.assertFalse(validity_triangle(100, 100, 100))

    def test_edge_valid(self):
        self.assertTrue(validity_triangle(90, 60, 30))

    def test_edge_invalid(self):
        self.assertFalse(validity_triangle(100, 100, 100))

    def test_boundary_valid(self):
        self.assertTrue(validity_triangle(179, 1, 0))

    def test_boundary_invalid(self):
        self.assertFalse(validity_triangle(181, 1, 0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            validity_triangle('a', 'b', 'c')
