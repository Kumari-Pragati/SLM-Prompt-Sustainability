import unittest
from mbpp_936_code import re_arrange_tuples

class TestRearrangeTuples(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['b', 'a', 'c']
        expected_result = [('b', 2), ('a', 1), ('c', 3)]
        self.assertEqual(re_arrange_tuples(test_list, ord_list), expected_result)

    def test_empty_list(self):
        test_list = []
        ord_list = ['b', 'a', 'c']
        expected_result = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), expected_result)

    def test_duplicate_keys(self):
        test_list = [('a', 1), ('b', 2), ('a', 3)]
        ord_list = ['b', 'a']
        expected_result = [('b', 2), ('a', 1)]
        self.assertEqual(re_arrange_tuples(test_list, ord_list), expected_result)

    def test_unordered_ord_list(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['b', 'a', 'c', 'd']
        expected_result = [('b', 2), ('a', 1), ('c', 3)]
        self.assertEqual(re_arrange_tuples(test_list, ord_list), expected_result)

    def test_missing_keys(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['d', 'e', 'f']
        expected_result = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), expected_result)
