import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_simple_even_length(self):
        self.assertTrue(even_position([2, 4, 6]))

    def test_simple_odd_length(self):
        self.assertTrue(even_position([1, 3, 5]))

    def test_empty_list(self):
        self.assertTrue(even_position([]))

    def test_single_element(self):
        self.assertTrue(even_position([0]))
        self.assertTrue(even_position([1]))

    def test_edge_cases(self):
        self.assertTrue(even_position([0, 2, 4, 6, 8]))
        self.assertTrue(even_position([1, 3, 5, 7, 9]))
        self.assertFalse(even_position([0, 1, 2, 3, 4]))
        self.assertFalse(even_position([1, 0, 1, 0, 1]))

    def test_negative_numbers(self):
        self.assertTrue(even_position([-2, -4, -6]))
        self.assertTrue(even_position([-1, -3, -5]))
        self.assertFalse(even_position([-1, -2, -3, -4, -5]))
        self.assertFalse(even_position([-1, 0, -1, 0, -1]))
