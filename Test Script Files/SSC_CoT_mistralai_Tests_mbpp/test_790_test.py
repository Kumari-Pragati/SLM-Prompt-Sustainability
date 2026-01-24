import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_even_position_normal(self):
        self.assertTrue(even_position([2, 4, 6, 8]))
        self.assertTrue(even_position([1, 3, 5, 7, 9]))

    def test_even_position_edge_cases(self):
        self.assertFalse(even_position([0, 2, 4, 6]))
        self.assertFalse(even_position([1, 3, 5, 7]))
        self.assertFalse(even_position([2, 4, 6, 8, 10]))
        self.assertFalse(even_position([2, 4, 6, 8, 10, 12]))

    def test_even_position_empty_list(self):
        self.assertIsNone(even_position([]))

    def test_even_position_single_element(self):
        self.assertTrue(even_position([0]))
        self.assertTrue(even_position([2]))
        self.assertFalse(even_position([1]))

    def test_even_position_negative_numbers(self):
        self.assertTrue(even_position([-2, -4, -6, -8]))
        self.assertFalse(even_position([-1, -3, -5, -7]))
