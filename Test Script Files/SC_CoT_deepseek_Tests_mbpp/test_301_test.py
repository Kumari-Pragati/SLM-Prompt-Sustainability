import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2}}), 2)

    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 0)

    def test_nested_dicts(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': 1}}}), 3)

    def test_dict_with_list(self):
        self.assertEqual(dict_depth({'a': [1, 2, 3]}), 1)

    def test_dict_with_mixed_types(self):
        self.assertEqual(dict_depth({'a': 1, 'b': [1, 2, 3], 'c': {'d': 4}}), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            dict_depth(123)
