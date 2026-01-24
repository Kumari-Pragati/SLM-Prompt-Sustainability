import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):
    def test_normal(self):
        self.assertFalse(validity_triangle(3, 4, 5))
        self.assertTrue(validity_triangle(3, 6, 7))
        self.assertFalse(validity_triangle(6, 7, 3))
        self.assertFalse(validity_triangle(4, 5, 6))
        self.assertFalse(validity_triangle(5, 4, 6))
        self.assertFalse(validity_triangle(6, 5, 4))

    def test_edge_and_boundary(self):
        self.assertFalse(validity_triangle(0, 0, 0))
        self.assertFalse(validity_triangle(0, 0, 181))
        self.assertFalse(validity_triangle(180, 0, 0))
        self.assertFalse(validity_triangle(0, 180, 0))
        self.assertFalse(validity_triangle(0, 0, 180))

        self.assertTrue(validity_triangle(179, 1, 170))
        self.assertTrue(validity_triangle(1, 179, 170))
        self.assertTrue(validity_triangle(179, 170, 1))
        self.assertTrue(validity_triangle(170, 179, 1))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, validity_triangle, -1, 2, 3)
        self.assertRaises(ValueError, validity_triangle, 2, -1, 3)
        self.assertRaises(ValueError, validity_triangle, 2, 3, -1)
