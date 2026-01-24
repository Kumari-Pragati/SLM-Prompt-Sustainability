import unittest
from mbpp_709_code import defaultdict
from 709_code import get_unique

class TestGetUnique(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('a', 1), ('b', 2), ('a', 1), ('c', 3)]
        expected_result = '{"1": 2, "2": 1, "3": 1}'
        self.assertEqual(get_unique(test_list), expected_result)

    def test_empty_list(self):
        test_list = []
        expected_result = '{"": 0}'
        self.assertEqual(get_unique(test_list), expected_result)

    def test_single_item(self):
        test_list = [('a', 1)]
        expected_result = '{"1": 1}'
        self.assertEqual(get_unique(test_list), expected_result)

    def test_duplicate_items(self):
        test_list = [('a', 1), ('a', 1), ('b', 2), ('b', 2)]
        expected_result = '{"1": 2, "2": 2}'
        self.assertEqual(get_unique(test_list), expected_result)

    def test_edge_case_empty_value(self):
        test_list = [('a', None), ('b', None)]
        expected_result = '{"None": 2}'
        self.assertEqual(get_unique(test_list), expected_result)
