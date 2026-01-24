import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2}}), 2)

    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 1)

    def test_single_level_dict(self):
        self.assertEqual(dict_depth({'a': 1}), 1)

    def test_nested_dict_with_same_depth(self):
        self.assertEqual(dict_depth({'a': {'b': 1}}), 2)

    def test_nested_dict_with_different_depth(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': 1}}}), 3)

    def test_nested_dict_with_multiple_levels(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': 1}}}}), 4)

    def test_dict_with_list_value(self):
        self.assertEqual(dict_depth({'a': [1, 2, 3]}), 1)

    def test_dict_with_integer_value(self):
        self.assertEqual(dict_depth(123), 0)

    def test_dict_with_string_value(self):
        self.assertEqual(dict_depth('abc'), 0)
