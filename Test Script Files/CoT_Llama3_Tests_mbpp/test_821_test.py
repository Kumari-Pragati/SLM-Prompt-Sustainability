import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):
    def test_empty_dicts(self):
        self.assertEqual(merge_dictionaries({}, {}), {})

    def test_single_dict(self):
        self.assertEqual(merge_dictionaries({'a': 1}, {}), {'a': 1})

    def test_two_dicts(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_dict_with_common_key(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 2}, {'a': 3, 'c': 4}), {'a': 1, 'b': 2, 'c': 4})

    def test_dict_with_common_key_and_value(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 2}, {'a': 3, 'c': 4}), {'a': 1, 'b': 2, 'c': 4})

    def test_dict_with_common_key_and_value_and_type(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 'hello'}, {'a': 3, 'c': 4}), {'a': 1, 'b': 'hello', 'c': 4})

    def test_dict_with_common_key_and_value_and_type_and_list(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 'hello'}, {'a': 3, 'c': [1, 2, 3]}), {'a': 1, 'b': 'hello', 'c': [1, 2, 3]})

    def test_dict_with_common_key_and_value_and_type_and_list_and_dict(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 'hello'}, {'a': 3, 'c': [1, 2, 3], 'd': {'e': 4}}), {'a': 1, 'b': 'hello', 'c': [1, 2, 3], 'd': {'e': 4}})
