import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertTrue(validity_triangle(3, 4, 10))
        self.assertTrue(validity_triangle(6, 8, 4))

    def test_invalid_triangle(self):
        self.assertFalse(validity_triangle(3, 4, 11))
        self.assertFalse(validity_triangle(0, 0, 0))
        self.assertFalse(validity_triangle(1, 2, 3))
        self.assertFalse(validity_triangle(-1, 2, 3))
        self.assertFalse(validity_triangle(3, 2, -1))
