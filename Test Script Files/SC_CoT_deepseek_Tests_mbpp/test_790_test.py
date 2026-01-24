import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(even_position([0, 1, 2, 3, 4, 5]))

    def test_empty_list(self):
        self.assertTrue(even_position([]))

    def test_single_element(self):
        self.assertTrue(even_position([0]))

    def test_odd_length_list(self):
        self.assertFalse(even_position([0, 1, 2, 3, 4]))

    def test_all_even_positions_are_even(self):
        self.assertTrue(even_position([2, 0, 4, 6, 8]))

    def test_all_even_positions_are_odd(self):
        self.assertFalse(even_position([1, 3, 5, 7, 9]))

    def test_mixed_even_and_odd_positions(self):
        self.assertFalse(even_position([1, 0, 3, 2, 5, 4]))

    def test_negative_numbers(self):
        self.assertTrue(even_position([-2, 0, -4, 2]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_position("not a list")
