import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'c', 'b']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('c', 3), ('b', 2)])

    def test_empty_test_list(self):
        test_list = []
        ord_list = ['a', 'b', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_empty_order_list(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_order_list_with_duplicates(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'a', 'b', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('a', 1), ('b', 2), ('c', 3)])

    def test_order_list_with_non_existent_keys(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'b', 'd']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('b', 2)])
