import unittest
from mbpp_612_code import zip

class TestMergeFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(merge([['a', 'b'], ['c', 'd']]), [['a', 'c'], ['b', 'd']])
        self.assertEqual(merge([['1', '2'], ['3', '4']]), [['1', '3'], ['2', '4']])
        self.assertEqual(merge([['A', 'B'], ['C', 'D']]), [['A', 'C'], ['B', 'D']])

    def test_edge_case_empty_list(self):
        self.assertEqual(merge([]), [])

    def test_edge_case_single_list(self):
        self.assertEqual(merge([['a']]), [['a']])

    def test_edge_case_single_element_lists(self):
        self.assertEqual(merge([['a'], ['b']]), [['a', 'b']])

    def test_edge_case_lists_of_different_lengths(self):
        self.assertEqual(merge([['a', 'b'], ['c']]), [['a', 'c'], ['b']])

    def test_corner_case_lists_of_different_types(self):
        self.assertEqual(merge([['a', 1], ['b', 2]]), [['a', 'b'], [1, 2]])
