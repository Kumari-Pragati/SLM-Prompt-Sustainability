import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertTrue(validity_triangle(3, 4, 10))
        self.assertTrue(validity_triangle(6, 8, 4))
        self.assertTrue(validity_triangle(12, 15, 16))

    def test_invalid_triangle(self):
        self.assertFalse(validity_triangle(3, 4, 11))
        self.assertFalse(validity_triangle(6, 8, 5))
        self.assertFalse(validity_triangle(12, 15, 15))

    def test_zero_or_negative_inputs(self):
        self.assertFalse(validity_triangle(0, 0, 0))
        self.assertFalse(validity_triangle(-1, 2, 3))
        self.assertFalse(validity_triangle(0, -1, 3))
        self.assertFalse(validity_triangle(3, 0, -1))

    def test_sum_greater_than_180(self):
        self.assertFalse(validity_triangle(17, 1, 169))
        self.assertFalse(validity_triangle(181, 1, 1))
        self.assertFalse(validity_triangle(1, 181, 1))
        self.assertFalse(validity_triangle(1, 1, 181))
