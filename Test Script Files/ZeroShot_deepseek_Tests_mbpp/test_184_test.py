import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificNum(unittest.TestCase):

    def test_greater_specificnum_all_greater(self):
        self.assertTrue(greater_specificnum([10, 20, 30], 5))

    def test_greater_specificnum_not_all_greater(self):
        self.assertFalse(greater_specificnum([10, 20, 30], 35))

    def test_greater_specificnum_empty_list(self):
        self.assertTrue(greater_specificnum([], 5))

    def test_greater_specificnum_all_equal(self):
        self.assertFalse(greater_specificnum([5, 5, 5], 5))

    def test_greater_specificnum_negative_numbers(self):
        self.assertTrue(greater_specificnum([-10, -5, -1], -5))
