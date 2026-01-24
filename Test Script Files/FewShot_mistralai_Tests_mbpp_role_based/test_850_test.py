import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertTrue(is_triangleexists(3, 4, 5))
        self.assertTrue(is_triangleexists(6, 8, 10))
        self.assertTrue(is_triangleexists(12, 16, 20))

    def test_sum_of_two_sides_greater_than_third(self):
        self.assertFalse(is_triangleexists(3, 4, 6))
        self.assertFalse(is_triangleexists(4, 5, 7))
        self.assertFalse(is_triangleexists(5, 6, 8))

    def test_sum_of_two_sides_less_than_third(self):
        self.assertFalse(is_triangleexists(3, 4, 7))
        self.assertFalse(is_triangleexists(4, 5, 9))
        self.assertFalse(is_triangleexists(5, 6, 11))

    def test_zero_or_negative_inputs(self):
        self.assertFalse(is_triangleexists(0, 0, 0))
        self.assertFalse(is_triangleexists(-1, 2, 3))
        self.assertFalse(is_triangleexists(0, 0, 181))

    def test_sum_of_sides_not_equal_to_180(self):
        self.assertFalse(is_triangleexists(3, 4, 5, 179))
        self.assertFalse(is_triangleexists(6, 8, 10, 178))
        self.assertFalse(is_triangleexists(12, 16, 20, 177))
