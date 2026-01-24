import unittest
from mbpp_899_code import check

class TestCheck(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_negative_numbers(self):
        self.assertTrue(check([5, 4, 3, 2, 1], 5))

    def test_mixed_numbers(self):
        self.assertFalse(check([1, 2, 3, 2, 1], 5))

    def test_single_number(self):
        self.assertTrue(check([1], 1))

    def test_empty_list(self):
        self.assertTrue(check([], 0))
