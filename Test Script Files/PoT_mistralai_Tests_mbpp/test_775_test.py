import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(odd_position([1, 3, 5, 7, 9]))
        self.assertTrue(odd_position([2, 4, 6, 8, 10]))

    def test_edge_case_empty(self):
        self.assertFalse(odd_position([]))

    def test_edge_case_single_element(self):
        self.assertTrue(odd_position([1]))
        self.assertFalse(odd_position([0]))

    def test_edge_case_even_length(self):
        self.assertFalse(odd_position([0, 2, 4, 6]))
        self.assertFalse(odd_position([1, 3, 5, 7, 9, 11]))

    def test_corner_case_odd_length_all_even(self):
        self.assertFalse(odd_position([2, 4, 6, 8, 10, 12]))

    def test_corner_case_odd_length_all_odd(self):
        self.assertTrue(odd_position([1, 3, 5, 7, 9, 11]))
