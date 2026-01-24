import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_triangleexists(60, 60, 60))

    def test_zero_side(self):
        self.assertFalse(is_triangleexists(0, 60, 60))
        self.assertFalse(is_triangleexists(60, 0, 60))
        self.assertFalse(is_triangleexists(60, 60, 0))

    def test_sum_not_180(self):
        self.assertFalse(is_triangleexists(60, 60, 61))

    def test_inequality_condition(self):
        self.assertFalse(is_triangleexists(120, 30, 30))
        self.assertFalse(is_triangleexists(30, 120, 30))
        self.assertFalse(is_triangleexists(30, 30, 120))

    def test_equal_sides(self):
        self.assertTrue(is_triangleexists(60, 60, 60))

    def test_large_numbers(self):
        self.assertTrue(is_triangleexists(100, 100, 80))
