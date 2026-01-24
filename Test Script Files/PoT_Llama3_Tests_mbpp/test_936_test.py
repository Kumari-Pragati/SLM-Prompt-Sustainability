import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'b', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('b', 2), ('c', 3)])

    def test_edge_case_empty_list(self):
        test_list = []
        ord_list = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_edge_case_empty_order_list(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_edge_case_empty_test_list(self):
        test_list = []
        ord_list = ['a', 'b', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_edge_case_order_list_with_duplicates(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'a', 'b', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('b', 2), ('c', 3)])

    def test_edge_case_order_list_with_duplicates_and_empty(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'a', 'b', 'c', '']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('b', 2), ('c', 3)])

    def test_edge_case_order_list_with_duplicates_and_empty_and_duplicates(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'a', 'b', 'c', '', 'a']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('b', 2), ('c', 3)])
