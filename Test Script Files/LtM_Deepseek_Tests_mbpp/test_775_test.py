import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):

    def test_simple_valid_input(self):
        self.assertTrue(odd_position([1, 3, 5]))

    def test_empty_input(self):
        self.assertTrue(odd_position([]))

    def test_all_even_positions(self):
        self.assertTrue(odd_position([0, 2, 4]))

    def test_all_odd_positions(self):
        self.assertTrue(odd_position([1, 3, 5]))

    def test_mixed_even_and_odd_positions(self):
        self.assertFalse(odd_position([1, 2, 3]))

    def test_negative_numbers(self):
        self.assertTrue(odd_position([-1, -3, -5]))

    def test_mixed_even_and_odd_numbers(self):
        self.assertFalse(odd_position([0, 1, 2]))
