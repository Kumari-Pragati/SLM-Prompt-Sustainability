import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        # Typical case: valid triangle with sides of 3, 4, 5
        self.assertTrue(validity_triangle(3, 4, 5))

    def test_invalid_triangle(self):
        # Invalid triangle: sides are not greater than 0
        self.assertFalse(validity_triangle(0, 0, 0))
        # Invalid triangle: total of sides is not equal to 180
        self.assertFalse(validity_triangle(3, 3, 121))
        # Invalid triangle: one side is greater than the sum of the other two
        self.assertFalse(validity_triangle(4, 3, 7))

    def test_degenerate_triangle(self):
        # Degenerate triangle: two sides are equal
        self.assertTrue(validity_triangle(3, 3, 6))
        # Degenerate triangle: one side is equal to 0
        self.assertTrue(validity_triangle(3, 0, 5))
