import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 1))
        self.assertTrue(greater_specificnum([10, 20, 30, 40, 50], 10))
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], 6))
        self.assertFalse(greater_specificnum([10, 20, 30, 40, 50], 51))

    def test_empty_list(self):
        self.assertTrue(greater_specificnum([], 0))

    def test_negative_numbers(self):
        self.assertTrue(greater_specificnum([-1, -2, -3, -4, -5], -4))
        self.assertFalse(greater_specificnum([-1, -2, -3, -4, -5], -6))

    def test_zero(self):
        self.assertTrue(greater_specificnum([0, 1, 2, 3, 4], 0))
        self.assertFalse(greater_specificnum([0, 1, 2, 3, 4], 1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            greater_specificnum("not a list", 1)
        with self.assertRaises(TypeError):
            greater_specificnum([1, 2, "not a number"], 1)
