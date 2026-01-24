import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):
    def test_even_length_odd_numbers(self):
        self.assertTrue(odd_position([1, 3, 5, 7]))

    def test_odd_length_odd_numbers(self):
        self.assertTrue(odd_position([1, 3, 5, 7, 9]))

    def test_even_length_even_numbers(self):
        self.assertFalse(odd_position([2, 4, 6, 8]))

    def test_odd_length_even_numbers(self):
        self.assertFalse(odd_position([2, 4, 6, 8, 10]))

    def test_empty_list(self):
        self.assertIsNone(odd_position([]))

    def test_single_number(self):
        self.assertIsNone(odd_position([1]))

    def test_all_zero(self):
        self.assertIsNone(odd_position([0]))
