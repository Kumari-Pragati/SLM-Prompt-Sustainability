import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    def test_is_woodall_true(self):
        self.assertTrue(is_woodall(1))

    def test_is_woodall_false(self):
        self.assertFalse(is_woodall(2))

    def test_is_woodall_even(self):
        self.assertFalse(is_woodall(4))

    def test_is_woodall_odd(self):
        self.assertFalse(is_woodall(3))

    def test_is_woodall_prime(self):
        self.assertTrue(is_woodall(7))

    def test_is_woodall_composite(self):
        self.assertFalse(is_woodall(6))

    def test_is_woodall_edge_case(self):
        self.assertFalse(is_woodall(0))
