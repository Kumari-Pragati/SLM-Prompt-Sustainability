import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificnum(unittest.TestCase):

    def test_greater_specificnum_positive(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 3))
        self.assertTrue(greater_specificnum([10, 20, 30, 40, 50], 30))
        self.assertTrue(greater_specificnum([5, 6, 7, 8, 9], 7))

    def test_greater_specificnum_negative(self):
        self.assertFalse(greater_specificnum([-1, -2, -3, -4, -5], 0))
        self.assertFalse(greater_specificnum([-10, -20, -30, -40, -50], -40))
        self.assertFalse(greater_specificnum([-5, -6, -7, -8, -9], -8))

    def test_greater_specificnum_empty(self):
        self.assertFalse(greater_specificnum([], 0))
        self.assertFalse(greater_specificnum([], 10))

    def test_greater_specificnum_single_element(self):
        self.assertTrue(greater_specificnum([5], 5))
        self.assertFalse(greater_specificnum([-5], -5))

    def test_greater_specificnum_all_elements_greater(self):
        self.assertTrue(greater_specificnum([10, 20, 30, 40, 50], 10))

    def test_greater_specificnum_all_elements_smaller(self):
        self.assertFalse(greater_specificnum([-10, -20, -30, -40, -50], 0))
