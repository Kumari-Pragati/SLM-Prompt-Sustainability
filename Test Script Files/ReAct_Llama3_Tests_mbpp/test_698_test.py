import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):

    def test_typical_case(self):
        test_dict = {'a': 1, 'c': 3, 'b': 2}
        expected_result = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_empty_dict(self):
        test_dict = {}
        expected_result = {}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_single_key_dict(self):
        test_dict = {'a': 1}
        expected_result = {'a': 1}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_dict_with_single_key(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        expected_result = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_dict_with_multiple_keys(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        expected_result = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_dict_with_negative_keys(self):
        test_dict = {'-1': 1, '0': 2, '1': 3}
        expected_result = {'-1': 1, '0': 2, '1': 3}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_dict_with_negative_values(self):
        test_dict = {'a': -1, 'b': 0, 'c': 1}
        expected_result = {'a': -1, 'b': 0, 'c': 1}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_dict_with_negative_keys_and_values(self):
        test_dict = {'-1': -1, '0': 0, '1': 1}
        expected_result = {'-1': -1, '0': 0, '1': 1}
        self.assertEqual(sort_dict_item(test_dict), expected_result)
