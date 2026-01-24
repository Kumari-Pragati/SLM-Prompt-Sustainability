import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 0)

    def test_single_level_dict(self):
        self.assertEqual(dict_depth({'a': 1, 'b': 2}), 1)

    def test_multi_level_dict(self):
        self.assertEqual(dict_depth({'a': {'b': 1, 'c': 2}, 'd': 3}), 2)

    def test_dict_with_non_dict_values(self):
        self.assertEqual(dict_depth({'a': 1, 'b': 2, 'c': {'d': 3}}), 1)

    def test_dict_with_empty_list(self):
        self.assertEqual(dict_depth({'a': [1, 2, 3]}), 0)

    def test_dict_with_non_dict_value_and_sub_dict(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2, 'd': 3}}), 2)
