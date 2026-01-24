import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(validity_triangle(60, 60, 60))

    def test_boundary_case(self):
        self.assertFalse(validity_triangle(180, 1, 1))

    def test_edge_case(self):
        self.assertFalse(validity_triangle(0, 0, 0))
        self.assertFalse(validity_triangle(181, 1, 1))
        self.assertFalse(validity_triangle(1, 181, 1))
        self.assertFalse(validity_triangle(1, 1, 181))

    def test_negative_values(self):
        self.assertFalse(validity_triangle(-1, -1, -1))
        self.assertFalse(validity_triangle(181, -1, -1))
        self.assertFalse(validity_triangle(-1, 181, -1))
        self.assertFalse(validity_triangle(-1, -1, 181))

    def test_non_integer_values(self):
        self.assertFalse(validity_triangle(60.5, 60, 60))
        self.assertFalse(validity_triangle(60, 60.5, 60))
        self.assertFalse(validity_triangle(60, 60, 60.5))

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            validity_triangle("60", 60, 60)
        with self.assertRaises(TypeError):
            validity_triangle(60, "60", 60)
        with self.assertRaises(TypeError):
            validity_triangle(60, 60, "60")
