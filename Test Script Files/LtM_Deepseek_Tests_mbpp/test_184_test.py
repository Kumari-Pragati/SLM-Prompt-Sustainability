import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 2))
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], 5))

    def test_empty_list(self):
        self.assertTrue(greater_specificnum([], 0))

    def test_single_element_list(self):
        self.assertTrue(greater_specificnum([5], 5))
        self.assertFalse(greater_specificnum([5], 6))

    def test_all_elements_equal(self):
        self.assertTrue(greater_specificnum([2, 2, 2, 2], 2))
        self.assertFalse(greater_specificnum([2, 2, 2, 2], 3))

    def test_all_elements_greater(self):
        self.assertTrue(greater_specificnum([2, 3, 4, 5], 1))

    def test_all_elements_less(self):
        self.assertFalse(greater_specificnum([1, 2, 3, 4], 5))

    def test_negative_numbers(self):
        self.assertTrue(greater_specificnum([-1, -2, -3, -4], -3))
        self.assertFalse(greater_specificnum([-1, -2, -3, -4], -5))
