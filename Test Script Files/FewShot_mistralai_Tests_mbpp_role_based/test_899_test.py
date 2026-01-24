import unittest
from mbpp_899_code import check

class TestCheck(unittest.TestCase):
    def test_increasing_sequence(self):
        self.assertTrue(check([1, 2, 3, 4], 4))

    def test_decreasing_sequence(self):
        self.assertFalse(check([4, 3, 2, 1], 4))

    def test_single_element(self):
        self.assertTrue(check([1], 1))

    def test_empty_list(self):
        self.assertRaises(ValueError, check, [], 0)

    def test_negative_numbers(self):
        self.assertTrue(check([-1, -2, -3], 3))

    def test_zero_element(self):
        self.assertTrue(check([0], 1))
        self.assertFalse(check([0, 0], 2))
