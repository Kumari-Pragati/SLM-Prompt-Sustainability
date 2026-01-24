import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(same_order([1, 2, 3], [2, 3, 1]))

    def test_edge_case_empty_list(self):
        self.assertTrue(same_order([], []))

    def test_edge_case_single_element(self):
        self.assertTrue(same_order([1], [1]))

    def test_edge_case_duplicates(self):
        self.assertTrue(same_order([1, 1, 2], [1, 2, 1]))

    def test_edge_case_order_matters(self):
        self.assertFalse(same_order([1, 2, 3], [3, 2, 1]))

    def test_edge_case_lists_of_different_lengths(self):
        self.assertFalse(same_order([1, 2, 3], [1, 2]))

    def test_edge_case_lists_with_duplicates(self):
        self.assertFalse(same_order([1, 1, 2, 2, 3], [1, 2, 3]))
