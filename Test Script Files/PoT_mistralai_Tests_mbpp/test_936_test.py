import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(re_arrange_tuples([('a', 1), ('b', 2), ('c', 3)], ['b', 'a', 'c']), [('b', 2), ('a', 1), ('c', 3)])

    def test_edge_case_empty_list(self):
        self.assertEqual(re_arrange_tuples([], ['a', 'b']), [])

    def test_edge_case_empty_ord_list(self):
        self.assertEqual(re_arrange_tuples([('a', 1), ('b', 2)], []), [])

    def test_edge_case_single_item_lists(self):
        self.assertEqual(re_arrange_tuples([('a', 1)], ['a']), [('a', 1)])
        self.assertEqual(re_arrange_tuples([('a', 1)], []), [])

    def test_edge_case_single_item_ord_list(self):
        self.assertEqual(re_arrange_tuples([('a', 1)], ['b']), [])

    def test_corner_case_duplicate_keys(self):
        self.assertEqual(re_arrange_tuples([('a', 1), ('a', 2)], ['a']), [('a', 1), ('a', 2)])

    def test_corner_case_duplicate_ord_list(self):
        self.assertEqual(re_arrange_tuples([('a', 1), ('b', 2)], ['a', 'a']), [('a', 1), ('a', 1)])
