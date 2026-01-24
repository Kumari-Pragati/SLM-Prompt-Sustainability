import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 0)

    def test_single_key_dict(self):
        self.assertEqual(dict_depth({'a': 1}), 1)

    def test_nested_dict(self):
        self.assertEqual(dict_depth({'a': {'b': 2, 'c': 3}}), 2)

    def test_dict_with_non_dict_values(self):
        self.assertEqual(dict_depth({'a': 1, 'b': 2, 'c': {'d': 3}}), 2)

    def test_dict_with_empty_list(self):
        self.assertEqual(dict_depth({'a': [1, 2, 3]}), 0)

    def test_dict_with_non_dict_values_and_empty_list(self):
        self.assertEqual(dict_depth({'a': 1, 'b': 2, 'c': [1, 2, 3]}), 0)

    def test_dict_with_non_dict_values_and_nested_dict(self):
        self.assertEqual(dict_depth({'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}), 2)

    def test_dict_with_non_dict_values_and_nested_dict_and_empty_list(self):
        self.assertEqual(dict_depth({'a': 1, 'b': 2, 'c': {'d': 3, 'e': [1, 2, 3]}}), 2)
