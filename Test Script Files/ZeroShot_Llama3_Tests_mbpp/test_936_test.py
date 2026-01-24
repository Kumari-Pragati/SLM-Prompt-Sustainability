import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):

    def test_re_arrange_tuples(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['c', 'a', 'b']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('c', 3), ('a', 1), ('b', 2)])

        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['b', 'a', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('b', 2), ('a', 1), ('c', 3)])

        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['c', 'b', 'a']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('c', 3), ('b', 2), ('a', 1)])

        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'b', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('b', 2), ('c', 3)])

        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['c', 'a', 'b', 'd']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('c', 3), ('a', 1), ('b', 2)])

        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'c', 'b']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('c', 3), ('b', 2)])

        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['b', 'c', 'a']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('b', 2), ('c', 3), ('a', 1)])

        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'b', 'c', 'd']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('b', 2), ('c', 3)])

    def test_re_arrange_tuples_empty_list(self):
        test_list = []
        ord_list = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_re_arrange_tuples_empty_order_list(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_re_arrange_tuples_empty_test_list(self):
        test_list = []
        ord_list = ['a', 'b', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])
