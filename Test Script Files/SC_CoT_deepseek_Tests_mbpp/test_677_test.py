import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(validity_triangle(60, 60, 60))

    def test_boundary_conditions(self):
        self.assertTrue(validity_triangle(0, 0, 180))
        self.assertFalse(validity_triangle(180, 0, 0))
        self.assertFalse(validity_triangle(0, 180, 0))
        self.assertFalse(validity_triangle(180, 180, 0))

    def test_edge_cases(self):
        self.assertTrue(validity_triangle(1, 1, 178))
        self.assertFalse(validity_triangle(1, 1, 179))
        self.assertFalse(validity_triangle(181, 0, 0))
        self.assertFalse(validity_triangle(0, 181, 0))
        self.assertFalse(validity_triangle(0, 0, 181))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            validity_triangle("a", 60, 60)
        with self.assertRaises(TypeError):
            validity_triangle(60, "b", 60)
        with self.assertRaises(TypeError):
            validity_triangle(60, 60, "c")
        with self.assertRaises(ValueError):
            validity_triangle(-1, 60, 60)
        with self.assertRaises(ValueError):
            validity_triangle(60, -1, 60)
        with self.assertRaises(ValueError):
            validity_triangle(60, 60, -1)
        with self.assertRaises(ValueError):
            validity_triangle(200, 60, 60)
        with self.assertRaises(ValueError):
            validity_triangle(60, 200, 60)
        with self.assertRaises(ValueError):
            validity_triangle(60, 60, 200)
