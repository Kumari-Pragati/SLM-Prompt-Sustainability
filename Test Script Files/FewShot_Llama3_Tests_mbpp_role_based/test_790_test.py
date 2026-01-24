import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_even_position_positive_numbers(self):
        self.assertTrue(even_position([2, 4, 6, 8]))

    def test_even_position_negative_numbers(self):
        self.assertTrue(even_position([-2, -4, -6, -8]))

    def test_even_position_mixed_numbers(self):
        self.assertTrue(even_position([1, 2, 3, 4]))

    def test_even_position_all_even_numbers(self):
        self.assertTrue(even_position([2, 4, 6, 8, 10]))

    def test_even_position_all_odd_numbers(self):
        self.assertFalse(even_position([1, 3, 5, 7]))

    def test_even_position_empty_list(self):
        self.assertTrue(even_position([]))

    def test_even_position_single_element_list(self):
        self.assertTrue(even_position([0]))

    def test_even_position_single_element_list_odd(self):
        self.assertFalse(even_position([1]))
