import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_isosceles_true(self):
        self.assertTrue(check_isosceles(3,3,5))
        self.assertTrue(check_isosceles(2,2,2))
        self.assertTrue(check_isosceles(10,10,20))

    def test_isosceles_false(self):
        self.assertFalse(check_isosceles(1,2,3))
        self.assertFalse(check_isosceles(4,5,6))
        self.assertFalse(check_isosceles(7,8,9))
