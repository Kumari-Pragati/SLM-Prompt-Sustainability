import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):

    def test_simple_valid(self):
        self.assertTrue(validity_triangle(3, 4, 10))
        self.assertTrue(validity_triangle(6, 7, 5))
        self.assertTrue(validity_triangle(12, 15, 3))

    def test_edge_cases(self):
        self.assertFalse(validity_triangle(0, 0, 0))
        self.assertFalse(validity_triangle(179, 1, 180))
        self.assertFalse(validity_triangle(181, 1, 179))
        self.assertFalse(validity_triangle(1, 1, 178))
        self.assertFalse(validity_triangle(180, 0, 0))
        self.assertFalse(validity_triangle(0, 180, 0))
        self.assertFalse(validity_triangle(0, 0, 180))

    def test_complex_cases(self):
        self.assertFalse(validity_triangle(1, 1, 177))
        self.assertFalse(validity_triangle(178, 1, 1))
        self.assertFalse(validity_triangle(1, 178, 1))
        self.assertFalse(validity_triangle(177, 178, 1))
        self.assertFalse(validity_triangle(-1, 2, 3))
        self.assertFalse(validity_triangle(2, -1, 3))
        self.assertFalse(validity_triangle(2, 3, -1))
