import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificNum(unittest.TestCase):
    def test_greater_than_single_number(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4], 2))

    def test_equal_to_single_number(self):
        self.assertFalse(greater_specificnum([1, 1, 3, 4], 1))

    def test_less_than_single_number(self):
        self.assertFalse(greater_specificnum([1, 0, 3, 4], 2))

    def test_empty_list(self):
        self.assertIsNone(greater_specificnum([]))

    def test_single_number_list(self):
        self.assertIsNone(greater_specificnum([1]))

    def test_negative_numbers(self):
        self.assertTrue(greater_specificnum([-1, -2, -3, -4], -5))

    def test_all_zero(self):
        self.assertFalse(greater_specificnum([0, 0, 0, 0], 1))
