import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_even_positions_in_even_length_list(self):
        self.assertTrue(even_position([2, 4, 6]))

    def test_even_positions_in_odd_length_list(self):
        self.assertTrue(even_position([1, 3, 4, 5]))

    def test_all_even_positions(self):
        self.assertTrue(even_position([2, 2, 2]))

    def test_all_odd_positions(self):
        self.assertFalse(even_position([1, 1, 1]))

    def test_empty_list(self):
        self.assertTrue(even_position([]))

    def test_single_element_list(self):
        self.assertTrue(even_position([0]))

    def test_all_zeroes(self):
        self.assertTrue(even_position([0, 0, 0]))

    def test_all_ones(self):
        self.assertFalse(even_position([1, 1, 1]))

    def test_mixed_even_and_odd_positions(self):
        self.assertFalse(even_position([1, 2, 3, 4]))
