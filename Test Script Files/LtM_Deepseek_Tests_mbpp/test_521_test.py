import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_simple_isosceles(self):
        self.assertTrue(check_isosceles(3, 3, 2))

    def test_edge_conditions(self):
        self.assertTrue(check_isosceles(0, 0, 0))
        self.assertFalse(check_isosceles(1, 2, 3))

    def test_complex_isosceles(self):
        self.assertTrue(check_isosceles(10, 10, 9))
        self.assertFalse(check_isosceles(5, 6, 7))
