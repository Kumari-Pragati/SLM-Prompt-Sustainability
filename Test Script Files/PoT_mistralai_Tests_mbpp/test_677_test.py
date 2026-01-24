import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertTrue(validity_triangle(3, 4, 5))
        self.assertTrue(validity_triangle(6, 7, 5))
        self.assertTrue(validity_triangle(6, 8, 10))

    def test_invalid_triangle(self):
        self.assertFalse(validity_triangle(3, 4, 6))
        self.assertFalse(validity_triangle(3, 6, 4))
        self.assertFalse(validity_triangle(4, 3, 5))
        self.assertFalse(validity_triangle(0, 3, 3))
        self.assertFalse(validity_triangle(3, 0, 3))
        self.assertFalse(validity_triangle(3, 3, 0))

    def test_sum_not_180(self):
        self.assertFalse(validity_triangle(3, 4, 7))
        self.assertFalse(validity_triangle(6, 7, 5))
        self.assertFalse(validity_triangle(6, 8, 4))
