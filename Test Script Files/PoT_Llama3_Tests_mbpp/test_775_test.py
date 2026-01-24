import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(odd_position([1, 2, 3, 4, 5]))

    def test_edge_case_empty_list(self):
        self.assertTrue(odd_position([]))

    def test_edge_case_single_element_list(self):
        self.assertTrue(odd_position([1]))

    def test_edge_case_even_length_list(self):
        self.assertFalse(odd_position([1, 2, 3, 4]))

    def test_edge_case_odd_length_list(self):
        self.assertTrue(odd_position([1, 2, 3]))

    def test_edge_case_mixed_length_list(self):
        self.assertFalse(odd_position([1, 2, 3, 4, 5, 6]))

    def test_edge_case_mixed_length_list_with_zero(self):
        self.assertFalse(odd_position([0, 1, 2, 3, 4, 5]))

    def test_edge_case_mixed_length_list_with_negative(self):
        self.assertFalse(odd_position([-1, 0, 1, 2, 3, 4]))

    def test_edge_case_mixed_length_list_with_zero_and_negative(self):
        self.assertFalse(odd_position([0, -1, 0, 1, 2, 3]))
