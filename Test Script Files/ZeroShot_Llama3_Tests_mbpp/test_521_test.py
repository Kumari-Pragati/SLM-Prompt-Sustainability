import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_isosceles(self):
        self.assertTrue(check_isosceles(1,2,3))
        self.assertTrue(check_isosceles(3,2,1))
        self.assertTrue(check_isosceles(2,1,3))
        self.assertTrue(check_isosceles(3,1,2))
        self.assertTrue(check_isosceles(1,3,2))
        self.assertTrue(check_isosceles(2,3,1))

    def test_not_isosceles(self):
        self.assertFalse(check_isosceles(1,2,4))
        self.assertFalse(check_isosceles(3,4,5))
        self.assertFalse(check_isosceles(2,3,6))
        self.assertFalse(check_isosceles(4,5,6))
        self.assertFalse(check_isosceles(1,3,5))
