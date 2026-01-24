import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):
    def test_typical_inputs(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'b', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('b', 2), ('c', 3)])

    def test_edge_case_empty_input(self):
        test_list = []
        ord_list = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_edge_case_empty_order(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_edge_case_empty_test(self):
        test_list = []
        ord_list = ['a', 'b', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_edge_case_order_longer_than_test(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'b', 'c', 'd']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('b', 2), ('c', 3)])

    def test_edge_case_order_shorter_than_test(self):
        test_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
        ord_list = ['a', 'b', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('b', 2), ('c', 3)])

    def test_invalid_input_non_list(self):
        test_list = 'not a list'
        ord_list = ['a', 'b', 'c']
        with self.assertRaises(TypeError):
            re_arrange_tuples(test_list, ord_list)

    def test_invalid_input_non_dict(self):
        test_list = [(1, 2), (3, 4)]
        ord_list = ['a', 'b', 'c']
        with self.assertRaises(TypeError):
            re_arrange_tuples(test_list, ord_list)
