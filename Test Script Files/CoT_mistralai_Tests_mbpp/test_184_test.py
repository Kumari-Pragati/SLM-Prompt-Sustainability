import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 2))
        self.assertTrue(greater_specificnum([10, 20, 30, 40, 50], 15))

    def test_zero_and_numbers(self):
        self.assertFalse(greater_specificnum([0, 1, 2, 3, 4], 5))
        self.assertFalse(greater_specificnum([-1, 0, 1, 2, 3], 4))

    def test_empty_list(self):
        self.assertIs(greater_specificnum([], 1), False)

    def test_single_number(self):
        self.assertTrue(greater_specificnum([5], 5))
        self.assertFalse(greater_specificnum([2], 5))

    def test_negative_numbers(self):
        self.assertTrue(greater_specificnum([-1, -2, -3, -4, -5], -6))
        self.assertFalse(greater_specificnum([-5, -4, -3, -2, -1], -6))

    def test_invalid_input(self):
        self.assertRaises(TypeError, greater_specificnum, [1, 2, 3], "not_a_number")
        self.assertRaises(TypeError, greater_specificnum, ["1", "2", "3"], 4)
