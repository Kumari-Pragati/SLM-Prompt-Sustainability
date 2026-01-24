import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_simple_dict(self):
        self.assertEqual(dict_depth({'a': 1}), 1)

    def test_nested_dict(self):
        self.assertEqual(dict_depth({'a': {'b': 1}}), 2)

    def test_nested_dict_with_list(self):
        self.assertEqual(dict_depth({'a': {'b': [1, 2, 3]}}), 3)

    def test_nested_dict_with_multiple_levels(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': 1}}}), 3)

    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 0)

    def test_dict_with_numbers(self):
        self.assertEqual(dict_depth({1: 2, 3: 4}), 1)

    def test_dict_with_lists(self):
        self.assertEqual(dict_depth({'a': [1, 2, 3], 'b': [4, 5, 6]}), 2)
