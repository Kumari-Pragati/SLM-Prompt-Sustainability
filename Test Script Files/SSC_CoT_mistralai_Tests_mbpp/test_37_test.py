import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(sort_mixed_list([1, 3, 'a', 'b', 2]), [1, 1, 2, 3, 'a', 'b'])

    def test_edge_case_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_edge_case_single_int(self):
        self.assertEqual(sort_mixed_list([1]), [1])

    def test_edge_case_single_str(self):
        self.assertEqual(sort_mixed_list(['a']), ['a'])

    def test_edge_case_single_mixed(self):
        self.assertEqual(sort_mixed_list([1, 'a']), [1, 'a'])

    def test_edge_case_int_str_mixed(self):
        self.assertEqual(sort_mixed_list([1, 'a', 2, 'b']), [1, 1, 2, 'a', 'b'])

    def test_edge_case_int_str_mixed_order(self):
        self.assertEqual(sort_mixed_list(['b', 'a', 2, 1]), ['b', 'a', 1, 2])

    def test_edge_case_list_of_lists(self):
        self.assertEqual(sort_mixed_list([[1], ['a'], [2], ['b']]), [[1], ['a'], [1, 2], 'b'])

    def test_edge_case_list_of_lists_of_lists(self):
        self.assertEqual(sort_mixed_list([[[1]], [['a']], [[2]], [['b']]]), [[[1]], [['a']], [[1, 2]], ['b']])
