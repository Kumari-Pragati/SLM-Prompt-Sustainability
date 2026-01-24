import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(re_order([1, 0, 2, 3, 0, 4]), [1, 2, 3, 4, 0, 0])

    def test_edge_case_empty_list(self):
        self.assertEqual(re_order([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(re_order([1]), [1])

    def test_edge_case_all_zeros(self):
        self.assertEqual(re_order([0, 0, 0]), [0, 0, 0])

    def test_edge_case_all_ones(self):
        self.assertEqual(re_order([1, 1, 1]), [1, 1, 1])

    def test_edge_case_mixed_list(self):
        self.assertEqual(re_order([1, 0, 2, 3, 4, 5]), [1, 2, 3, 4, 5, 0])

    def test_edge_case_reversed_list(self):
        self.assertEqual(re_order([5, 4, 3, 2, 1, 0]), [5, 4, 3, 2, 1, 0])

    def test_edge_case_duplicates(self):
        self.assertEqual(re_order([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])
