import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(validity_triangle(60, 60, 60))

    def test_edge_case(self):
        self.assertTrue(validity_triangle(0, 0, 0))

    def test_boundary_case(self):
        self.assertFalse(validity_triangle(180, 0, 0))
        self.assertFalse(validity_triangle(0, 180, 0))
        self.assertFalse(validity_triangle(0, 0, 180))
        self.assertFalse(validity_triangle(90, 90, 90))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            validity_triangle("60", 60, 60)
        with self.assertRaises(TypeError):
            validity_triangle(60, "60", 60)
        with self.assertRaises(TypeError):
            validity_triangle(60, 60, "60")
        with self.assertRaises(ValueError):
            validity_triangle(-1, 1, 1)
        with self.assertRaises(ValueError):
            validity_triangle(1, -1, 1)
        with self.assertRaises(ValueError):
            validity_triangle(1, 1, -1)
