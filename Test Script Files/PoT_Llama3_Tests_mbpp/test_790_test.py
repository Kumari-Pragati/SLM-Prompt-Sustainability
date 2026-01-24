import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(even_position([0, 1, 2, 3, 4, 5]))

    def test_edge_case_empty_list(self):
        self.assertTrue(even_position([]))

    def test_edge_case_single_element_list(self):
        self.assertTrue(even_position([0]))

    def test_edge_case_all_even_list(self):
        self.assertTrue(even_position([0, 2, 4, 6, 8]))

    def test_edge_case_all_odd_list(self):
        self.assertTrue(even_position([1, 3, 5, 7, 9]))

    def test_edge_case_mixed_list(self):
        self.assertTrue(even_position([0, 1, 2, 3, 4, 5]))

    def test_edge_case_all_zeros_list(self):
        self.assertTrue(even_position([0, 0, 0, 0, 0]))

    def test_edge_case_all_ones_list(self):
        self.assertFalse(even_position([1, 1, 1, 1, 1]))

    def test_edge_case_mixed_with_zeros_list(self):
        self.assertTrue(even_position([0, 1, 2, 3, 0]))

    def test_edge_case_mixed_with_ones_list(self):
        self.assertFalse(even_position([1, 0, 1, 0, 1]))
