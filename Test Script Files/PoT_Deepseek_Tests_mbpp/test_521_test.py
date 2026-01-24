import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_isosceles(3, 3, 2))
        self.assertTrue(check_isosceles(2, 3, 2))
        self.assertTrue(check_isosceles(3, 2, 3))

    def test_edge_cases(self):
        self.assertFalse(check_isosceles(1, 2, 3))
        self.assertFalse(check_isosceles(1, 1, 1))
        self.assertFalse(check_isosceles(0, 0, 0))

    def test_corner_cases(self):
        self.assertTrue(check_isosceles(0, 0, 0))
        self.assertTrue(check_isosceles(-1, -1, -2))
        self.assertTrue(check_isosceles(float('inf'), float('inf'), float('inf')))
        self.assertFalse(check_isosceles(float('nan'), float('nan'), float('nan')))
