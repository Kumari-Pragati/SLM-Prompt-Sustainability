import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_positive_sequence(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_zero_sequence(self):
        self.assertTrue(check([0, 0, 0, 0, 0], 5))

    def test_negative_sequence(self):
        self.assertTrue(check([-1, -2, -3, -4, -5], 5))

    def test_mixed_sequence(self):
        self.assertTrue(check([1, -2, 3, -4, 5], 5))

    def test_single_element(self):
        self.assertTrue(check([1], 1))

    def test_empty_list(self):
        self.assertFalse(check([], 0))

    def test_negative_difference_in_positive_sequence(self):
        self.assertFalse(check([1, 2, 1], 3))

    def test_positive_difference_in_negative_sequence(self):
        self.assertFalse(check([-1, -2, -3], 3))

    def test_zero_difference(self):
        self.assertTrue(check([1, 1, 1], 3))
