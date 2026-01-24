import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificnum(unittest.TestCase):
    def test_true(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 3))

    def test_false(self):
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], 6))

    def test_all_true(self):
        self.assertTrue(greater_specificnum([5, 5, 5, 5, 5], 5))

    def test_all_false(self):
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], 10))

    def test_mixed(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 2))

    def test_empty_list(self):
        self.assertFalse(greater_specificnum([], 5))

    def test_num_is_zero(self):
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], 0))

    def test_num_is_negative(self):
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], -1))
