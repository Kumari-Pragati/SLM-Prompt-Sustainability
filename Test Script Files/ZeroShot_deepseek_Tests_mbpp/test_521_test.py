import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_isosceles_true(self):
        self.assertTrue(check_isosceles(3, 4, 4))
        self.assertTrue(check_isosceles(5, 5, 6))
        self.assertTrue(check_isosceles(7, 7, 8))

    def test_isosceles_false(self):
        self.assertFalse(check_isosceles(1, 2, 3))
        self.assertFalse(check_isosceles(4, 4, 4))
        self.assertFalse(check_isosceles(5, 5, 5))
