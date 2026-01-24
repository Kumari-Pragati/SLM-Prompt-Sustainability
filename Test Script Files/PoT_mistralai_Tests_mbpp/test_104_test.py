import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(sort_sublists([[3, 'b'], [1, 'a'], [4, 'd'], [1, 'a']]), [[[1, 'a'], [1, 'a']], [['b', 3]], [['d', 4]]])

    def test_edge_case_empty_list(self):
        self.assertListEqual(sort_sublists([]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(sort_sublists([[1, 'a']]), [[[1, 'a']]])

    def test_edge_case_single_element_different_order(self):
        self.assertListEqual(sort_sublists([['a', 1]]), [[['a', 1]]])

    def test_edge_case_negative_numbers(self):
        self.assertListEqual(sort_sublists([[-3, 'b'], [1, 'a'], [-4, 'd'], [1, 'a']]), [[[-4, 'd'], [-3, 'b']], [['a', 1]], [['a', 1]]])

    def test_corner_case_mixed_types(self):
        self.assertListEqual(sort_sublists([[3, 'b'], [1, 'a'], [4, 'd'], [1, 'a'], [1, None]]), [[[1, 'a'], [1, 'a']], [['b', 3]], [['d', 4]], [['a', 1], None]])
