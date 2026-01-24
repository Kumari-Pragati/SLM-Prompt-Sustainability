import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(validity_triangle(60, 60, 60))

    def test_invalid_triangle(self):
        self.assertFalse(validity_triangle(120, 30, 30))

    def test_sum_not_180(self):
        self.assertFalse(validity_triangle(100, 70, 10))

    def test_negative_values(self):
        self.assertFalse(validity_triangle(-10, 20, 30))

    def test_zero_values(self):
        self.assertFalse(validity_triangle(0, 0, 0))
