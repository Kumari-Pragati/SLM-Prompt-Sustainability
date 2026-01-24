import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_simple_isosceles(self):
        self.assertTrue(check_isosceles(3, 3, 2))
        self.assertTrue(check_isosceles(2, 1, 2))
        self.assertTrue(check_isosceles(1, 2, 1))

    def test_edge_conditions(self):
        self.assertTrue(check_isosceles(0, 0, 0))
        self.assertTrue(check_isosceles(1, 1, 1))
        self.assertTrue(check_isosceles(100, 100, 1))
        self.assertTrue(check_isosceles(1, 100, 100))

    def test_complex_isosceles(self):
        self.assertTrue(check_isosceles(10, 10, 9))
        self.assertTrue(check_isosceles(10, 9, 10))
        self.assertTrue(check_isosceles(9, 10, 10))

    def test_non_isosceles(self):
        self.assertFalse(check_isosceles(1, 2, 3))
        self.assertFalse(check_isosceles(3, 2, 1))
        self.assertFalse(check_isosceles(2, 3, 1))
