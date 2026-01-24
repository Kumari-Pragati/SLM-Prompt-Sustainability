import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):
    def test_even_number(self):
        self.assertFalse(is_woodall(2))

    def test_odd_number(self):
        self.assertTrue(is_woodall(1))

    def test_power_of_two(self):
        self.assertTrue(is_woodall(8))

    def test_power_of_two_plus_one(self):
        self.assertFalse(is_woodall(9))

    def test_power_of_two_plus_two(self):
        self.assertTrue(is_woodall(16))

    def test_power_of_two_plus_three(self):
        self.assertFalse(is_woodall(17))

    def test_negative_number(self):
        self.assertFalse(is_woodall(-2))

    def test_zero(self):
        self.assertFalse(is_woodall(0))
