import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(even_position([2, 4, 6, 8]))
        self.assertTrue(even_position([1, 3, 5, 7]))

    def test_edge_case_empty_list(self):
        self.assertFalse(even_position([]))

    def test_edge_case_single_element(self):
        self.assertTrue(even_position([0]))
        self.assertTrue(even_position([2]))
        self.assertFalse(even_position([1]))

    def test_edge_case_odd_length(self):
        self.assertFalse(even_position([0, 1]))
        self.assertFalse(even_position([1, 2, 3]))
        self.assertTrue(even_position([2, 4, 6, 7]))

    def test_corner_case_mixed_even_odd(self):
        self.assertFalse(even_position([0, 1, 2, 3, 4, 5, 6]))
        self.assertTrue(even_position([2, 4, 6, 0, 1, 3, 5]))
