import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_typical_case(self):
        data = [(1, 'a'), (3, 'b'), (2, 'c'), (4, 'd')]
        self.assertEqual(index_on_inner_list(data, 0), [(1, 'a'), (2, 'c'), (3, 'b'), (4, 'd')])
        self.assertEqual(index_on_inner_list(data, 1), [(3, 'b'), (2, 'c'), (4, 'd'), (1, 'a')])

    def test_edge_case_empty_list(self):
        self.assertEqual(index_on_inner_list([], 0), [])

    def test_edge_case_single_element(self):
        data = [(1, 'a')]
        self.assertEqual(index_on_inner_list(data, 0), [(1, 'a')])

    def test_edge_case_negative_index(self):
        data = [(1, 'a'), (3, 'b'), (2, 'c'), (4, 'd')]
        with self.assertRaises(IndexError):
            index_on_inner_list(data, -1)

    def test_edge_case_out_of_range_index(self):
        data = [(1, 'a'), (3, 'b'), (2, 'c'), (4, 'd')]
        with self.assertRaises(IndexError):
            index_on_inner_list(data, len(data))
