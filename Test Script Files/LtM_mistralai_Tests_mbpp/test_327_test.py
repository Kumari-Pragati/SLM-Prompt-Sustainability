import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_simple_isosceles(self):
        self.assertTrue(check_isosceles(1, 1, 1))
        self.assertTrue(check_isosceles(2, 2, 2))
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_edge_cases(self):
        self.assertTrue(check_isosceles(0, 0, 0))
        self.assertTrue(check_isosceles(1, 1, 0))
        self.assertTrue(check_isosceles(0, 1, 1))
        self.assertTrue(check_isosceles(1, 0, 1))
        self.assertTrue(check_isosceles(1, 1, -1))
        self.assertTrue(check_isosceles(-1, 1, 1))
        self.assertTrue(check_isosceles(1, -1, 1))
        self.assertTrue(check_isosceles(1, 1, -1))

    def test_non_isosceles(self):
        self.assertFalse(check_isosceles(1, 2, 3))
        self.assertFalse(check_isosceles(2, 1, 3))
        self.assertFalse(check_isosceles(2, 3, 1))
        self.assertFalse(check_isosceles(3, 2, 1))
        self.assertFalse(check_isosceles(3, 1, 2))
        self.assertFalse(check_isosceles(1, 3, 2))
        self.assertFalse(check_isosceles(2, 3, 1))
        self.assertFalse(check_isosceles(3, 2, 1))
