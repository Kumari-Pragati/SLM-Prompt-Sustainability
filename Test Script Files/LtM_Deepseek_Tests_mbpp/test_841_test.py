import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(get_inv_count([1, 20, 6, 4, 5], 5), 5)

    def test_edge_condition_empty_array(self):
        self.assertEqual(get_inv_count([], 0), 0)

    def test_edge_condition_single_element(self):
        self.assertEqual(get_inv_count([1], 1), 0)

    def test_boundary_condition_minimum_value(self):
        self.assertEqual(get_inv_count([-1000000000], 1), 0)

    def test_boundary_condition_maximum_value(self):
        self.assertEqual(get_inv_count([1000000000], 1), 0)

    def test_complex_input(self):
        self.assertEqual(get_inv_count([4, 3, 2, 1], 4), 6)
