import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(validity_triangle(60, 60, 60))

    def test_boundary_conditions(self):
        self.assertTrue(validity_triangle(0, 0, 0))
        self.assertTrue(validity_triangle(180, 0, 0))
        self.assertTrue(validity_triangle(0, 180, 0))
        self.assertTrue(validity_triangle(0, 0, 180))
        self.assertTrue(validity_triangle(90, 90, 0))
        self.assertTrue(validity_triangle(90, 0, 90))
        self.assertTrue(validity_triangle(0, 90, 90))

    def test_edge_cases(self):
        self.assertFalse(validity_triangle(181, 0, 0))
        self.assertFalse(validity_triangle(-1, 0, 0))
        self.assertFalse(validity_triangle(0, 181, 0))
        self.assertFalse(validity_triangle(0, -1, 0))
        self.assertFalse(validity_triangle(0, 0, 181))
        self.assertFalse(validity_triangle(0, 0, -1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            validity_triangle("60", 60, 60)
        with self.assertRaises(TypeError):
            validity_triangle(60, "60", 60)
        with self.assertRaises(TypeError):
            validity_triangle(60, 60, "60")
        with self.assertRaises(TypeError):
            validity_triangle(60, 60, 60, 60)
