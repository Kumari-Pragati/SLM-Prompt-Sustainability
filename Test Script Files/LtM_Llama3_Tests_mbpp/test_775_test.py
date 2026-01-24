import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(odd_position([1, 2, 3, 4, 5]))
        self.assertTrue(odd_position([0, 2, 4, 6, 8]))
        self.assertTrue(odd_position([1, 3, 5, 7, 9]))

    def test_empty(self):
        self.assertFalse(odd_position([]))

    def test_single(self):
        self.assertFalse(odd_position([1]))

    def test_all_odd(self):
        self.assertTrue(odd_position([1, 3, 5, 7, 9]))

    def test_all_even(self):
        self.assertFalse(odd_position([2, 4, 6, 8, 10]))

    def test_mixed(self):
        self.assertFalse(odd_position([1, 2, 3, 4, 5]))
