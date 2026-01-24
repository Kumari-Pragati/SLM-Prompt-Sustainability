import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):
    def test_rearrange_tuples_with_valid_inputs(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['b', 'a', 'c']
        expected_output = [('b', 2), ('a', 1), ('c', 3)]
        self.assertEqual(re_arrange_tuples(test_list, ord_list), expected_output)

    def test_rearrange_tuples_with_empty_lists(self):
        test_list = []
        ord_list = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_rearrange_tuples_with_single_item_lists(self):
        test_list = [('a', 1)]
        ord_list = ['a']
        expected_output = [('a', 1)]
        self.assertEqual(re_arrange_tuples(test_list, ord_list), expected_output)

    def test_rearrange_tuples_with_invalid_input(self):
        with self.assertRaises(KeyError):
            re_arrange_tuples([('a', 1), ('b', 2)], ['c'])
