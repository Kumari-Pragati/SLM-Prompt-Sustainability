import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(validity_triangle(3, 4, 5))
        self.assertTrue(validity_triangle(6, 8, 10))
        self.assertTrue(validity_triangle(12, 16, 20))

    def test_invalid_triangle(self):
        self.assertFalse(validity_triangle(3, 4, 6))
        self.assertFalse(validity_triangle(6, 8, 9))
        self.assertFalse(validity_triangle(12, 16, 21))

    def test_degenerate_triangle(self):
        self.assertFalse(validity_triangle(0, 0, 0))
        self.assertFalse(validity_triangle(0, 0, 1))
        self.assertFalse(validity_triangle(1, 0, 0))
